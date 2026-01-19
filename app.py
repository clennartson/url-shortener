from flask import Flask, render_template, request, redirect, jsonify
import psycopg2
import random
import string

app = Flask(__name__)

# Database connection
def get_db():
    return psycopg2.connect(
        database="urlshortener",
        user="appuser",
        password="dev_password_123",
        host="localhost"
    )

# Generate random short code
def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# API: Shorten URL
@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')
    custom_code = data.get('custom_code')
    
    if not original_url:
        return jsonify({'error': 'URL required'}), 400
    
    if custom_code:
        if len(custom_code) < 3:
            return jsonify({'error': 'Custom code must be at least 3 characters'}), 400
        if not custom_code.isalnum():
            return jsonify({'error': 'Custom code can only contain letters and numbers'}), 400
        short_code = custom_code
    else:
        short_code = generate_short_code()
    
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO urls (original_url, short_code) VALUES (%s, %s) RETURNING short_code",
            (original_url, short_code)
        )
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({
            'short_url': f'http://localhost:5000/{result[0]}',
            'short_code': result[0]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Redirect short URL
@app.route('/<short_code>')
def redirect_url(short_code):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "UPDATE urls SET clicks = clicks + 1 WHERE short_code = %s RETURNING original_url",
            (short_code,)
        )
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        
        if result:
            return redirect(result[0])
        return jsonify({'error': 'URL not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get stats
@app.route('/api/stats/<short_code>')
def get_stats(short_code):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "SELECT original_url, clicks, created_at FROM urls WHERE short_code = %s",
            (short_code,)
        )
        result = cur.fetchone()
        cur.close()
        conn.close()
        
        if result:
            return jsonify({
                'original_url': result[0],
                'clicks': result[1],
                'created_at': str(result[2])
            })
        return jsonify({'error': 'Not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)