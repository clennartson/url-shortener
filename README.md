# URL Shortener

A simple, fast URL shortening service built with Flask and PostgreSQL.

## Features

- 🔗 Shorten long URLs into memorable short links
- 🎨 Custom short codes (choose your own!)
- 📊 Click tracking and analytics
- ⚡ Fast redirects with database indexing
- 🎯 Clean, responsive UI

## Tech Stack

- **Backend:** Python 3, Flask
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Docker (coming soon!)

## Local Setup

### Prerequisites

- Python 3.10+
- PostgreSQL 14+

### Installation

1. Clone the repository
```bash
git clone https://github.com/clennartson/url-shortener.git
cd url-shortener
```

2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up database
```bash
sudo -u postgres psql -c "CREATE DATABASE urlshortener;"
sudo -u postgres psql -c "CREATE USER appuser WITH PASSWORD 'dev_password_123';"
sudo -u postgres psql -d urlshortener -f schema.sql
```

5. Run the application
```bash
python app.py
```

6. Open browser to `http://localhost:5000`

## Usage

### Shorten a URL

1. Enter your long URL
2. (Optional) Choose a custom short code
3. Click "Shorten URL"
4. Share your short link!

### API Endpoints

- `POST /api/shorten` - Create short URL
- `GET /:code` - Redirect to original URL
- `GET /api/stats/:code` - Get URL statistics

## Project Structure
```
url-shortener/
├── app.py              # Flask application
├── schema.sql          # Database schema
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Frontend UI
└── README.md          # This file
```

## Roadmap

- [ ] Docker containerization
- [ ] AWS deployment
- [ ] QR code generation
- [ ] Analytics dashboard
- [ ] User authentication
- [ ] URL expiration

## Learning Journey

This project is part of my cloud computing learning path. Follow my progress:

- Day 1: Built full-stack application ✅
- Day 2: Git, GitHub, Docker ⏳
- Day 3: AWS deployment
- Day 4: Kubernetes
- Day 5: CI/CD pipeline

## License

MIT

## Author

Chase Lennartson - Aspiring Cloud Engineer

---

**Built while learning cloud computing!** 🚀
