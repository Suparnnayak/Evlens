# Event Review Summarizer 🎯

A full-stack AI-powered application for analyzing event reviews from CSV files and generating comprehensive summaries with sentiment analysis.

![Gold and White UI](https://img.shields.io/badge/UI-Gold%20%26%20White-FFD700?style=flat-square)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat-square&logo=fastapi)
![React](https://img.shields.io/badge/Frontend-React-61DAFB?style=flat-square&logo=react)

## ✨ Features

- 🔐 **User Authentication** - JWT-based secure authentication
- 📊 **CSV Analysis** - Upload and analyze event review CSV files
- 🤖 **AI-Powered Summaries** - Generate intelligent summaries using transformer models
- 📈 **Sentiment Analysis** - Comprehensive sentiment breakdown with visualizations
- 💡 **Key Insights** - Automatically extract actionable insights
- 🎨 **Modern UI** - Beautiful gold and white theme with responsive design
- 📥 **Export Results** - Download analysis results as JSON
- 🔍 **Smart Search** - Functional search bar with AI Analyze feature

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/event-review-summarizer.git
cd event-review-summarizer
```

2. **Backend Setup**
```bash
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
# source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
python run.py
```

3. **Frontend Setup** (in a new terminal)
```bash
cd frontend
npm install
npm run dev
```

4. **Access the Application**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 📁 Project Structure

```
event-review-summarizer/
├── backend/          # FastAPI backend
│   ├── main.py       # API entry point
│   ├── auth.py       # Authentication
│   ├── ml_service.py # ML pipeline
│   └── requirements.txt
├── frontend/         # React frontend
│   ├── src/
│   │   ├── pages/    # Page components
│   │   └── components/
│   └── package.json
├── ML/               # ML models and analysis
│   └── src/
│       ├── analyzer.py
│       └── summarizer.py
└── README.md
```

## 📊 CSV Format

Your CSV file should have this structure:

```csv
event_name,review_text
TechFest 2025,"Great event with amazing speakers!"
MusicFest 2025,"The sound quality could be better."
```

Sample CSV files are included in the repository root.

## 🎨 UI Features

- **Gold & White Theme** - Elegant and modern design
- **Responsive Layout** - Works on all devices
- **Interactive Charts** - Beautiful data visualizations
- **Real-time Analysis** - Fast processing with loading states
- **Error Handling** - User-friendly error messages

## 🔧 Technology Stack

### Backend
- FastAPI - Modern Python web framework
- SQLAlchemy - Database ORM
- Transformers - AI model for summarization
- TextBlob - Sentiment analysis
- JWT - Authentication

### Frontend
- React 18 - UI library
- Vite - Build tool
- Tailwind CSS - Styling
- Recharts - Data visualization
- Axios - HTTP client

## 📚 Documentation

- [DEPLOYMENT.md](./DEPLOYMENT.md) - Complete deployment guide
- [QUICK_DEPLOY.md](./QUICK_DEPLOY.md) - Quick deployment reference
- [GIT_PUSH_INSTRUCTIONS.md](./GIT_PUSH_INSTRUCTIONS.md) - GitHub setup
- [SAMPLE_CSV_FILES_README.md](./SAMPLE_CSV_FILES_README.md) - Sample data guide

## 🚀 Deployment

### Recommended Setup
- **Frontend**: Deploy on [Vercel](https://vercel.com)
- **Backend**: Deploy on [Railway](https://railway.app) or [Render](https://render.com)

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed instructions.

## 📝 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login and get token
- `GET /api/auth/me` - Get current user

### Analysis
- `POST /api/analyze` - Upload CSV and get analysis (requires auth)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License

## 👥 Team

Team EVLENS

---

**Made with ❤️ using FastAPI and React**
