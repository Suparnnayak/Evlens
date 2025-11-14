# Setup Guide

## Quick Start

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

### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### 3. Access the Application

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## First User

1. Go to http://localhost:3000
2. Click "Sign up" to create an account
3. Login with your credentials
4. Upload a CSV file with event reviews
5. Click "Analyze Reviews" to generate summary

## Troubleshooting

### Backend Issues

- **Import errors**: Make sure you're in the backend directory and virtual environment is activated
- **Database errors**: Delete `event_summarizer.db` and restart the server
- **Model download**: First run may take time to download the ML model

### Frontend Issues

- **Port already in use**: Change the port in `vite.config.js`
- **API connection errors**: Make sure backend is running on port 8000
- **Build errors**: Delete `node_modules` and run `npm install` again

## Development

### Running Tests

```bash
# Backend tests (if available)
cd backend
pytest

# Frontend tests (if available)
cd frontend
npm test
```

### Code Formatting

```bash
# Backend
black backend/
isort backend/

# Frontend
npm run format
```

