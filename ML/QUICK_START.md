# Quick Start Guide

## Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

## Setup (5 minutes)

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
```

Backend will run on `http://localhost:8000`

### 2. Frontend Setup

Open a new terminal:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will run on `http://localhost:3000`

### 3. Access the Application

1. Open browser and go to `http://localhost:3000`
2. Click "Sign up" to create an account
3. Login with your credentials
4. Upload a CSV file with event reviews
5. Click "Analyze Reviews" to generate summary

## CSV Format

Your CSV file should have this structure:

```csv
event_name,review_text
TechFest 2025,"Great event with amazing speakers!"
MusicFest 2025,"The sound quality could be better."
Hackathon 2025,"Well-organized event with helpful mentors."
```

## Troubleshooting

### Backend Issues
- **Import errors**: Make sure you're in the `backend` directory and virtual environment is activated
- **Database errors**: Delete `event_summarizer.db` and restart the server
- **Model download**: First run may take time to download the ML model (250MB)

### Frontend Issues
- **Port already in use**: Change port in `vite.config.js`
- **API connection errors**: Make sure backend is running on port 8000
- **Build errors**: Delete `node_modules` and run `npm install` again

## Next Steps

- Check `README.md` for detailed documentation
- Check `ML_IMPROVEMENTS.md` for ML improvements and suggestions
- Check `SETUP.md` for detailed setup instructions

## API Documentation

Once the backend is running, visit:
- API Docs: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc

## Support

For issues or questions, please check the documentation or create an issue.

