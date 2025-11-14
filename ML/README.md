# Event Review Summarizer

A full-stack application for analyzing event reviews from CSV files and generating AI-powered summaries with sentiment analysis.

## Features

- 🔐 User authentication (JWT-based)
- 📊 CSV file upload and analysis
- 🤖 AI-powered event summary generation
- 📈 Sentiment analysis with visualizations
- 🎨 Modern, responsive UI/UX
- 📥 Download results as JSON

## Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM for database operations
- **JWT** - Authentication tokens
- **Transformers** - AI model for summarization (google/flan-t5-base)
- **TextBlob** - Sentiment analysis
- **Pandas** - CSV processing

### Frontend
- **React** - UI library
- **Vite** - Build tool
- **Tailwind CSS** - Styling
- **Recharts** - Data visualization
- **Axios** - HTTP client
- **React Router** - Navigation

## Project Structure

```
.
├── backend/           # FastAPI backend
│   ├── main.py       # API entry point
│   ├── auth.py       # Authentication utilities
│   ├── database.py   # Database configuration
│   ├── models.py     # Database models
│   ├── schemas.py    # Pydantic schemas
│   └── ml_service.py # ML pipeline service
├── frontend/         # React frontend
│   ├── src/
│   │   ├── pages/    # Page components
│   │   ├── components/ # Reusable components
│   │   └── contexts/ # React contexts
│   └── package.json
├── src/              # Original ML code
│   ├── analyzer.py   # CSV analysis
│   └── summarizer.py # Summary generation
└── requirements.txt  # Python dependencies
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the backend server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## Usage

1. **Register/Login**: Create an account or login with existing credentials
2. **Upload CSV**: Upload a CSV file with event reviews (format: `event_name, review_text`)
3. **Analyze**: Click "Analyze Reviews" to process the file
4. **View Results**: See the generated summary, sentiment analysis, and insights
5. **Download**: Download the results as JSON

## CSV Format

The CSV file should have the following structure:

```csv
event_name,review_text
TechFest 2025,"Great event with amazing speakers!"
MusicFest 2025,"The sound quality could be better."
```

## ML Improvements Made

1. **All Reviews Processing**: Now processes ALL reviews, not just samples
2. **Lazy Model Loading**: Models are loaded only when needed
3. **Improved Sentiment Analysis**: More nuanced sentiment classification
4. **Better Error Handling**: Comprehensive error handling and logging
5. **Key Insights Extraction**: Automatically extracts key insights from reviews
6. **Performance Optimization**: Better text processing and chunking

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and get access token
- `GET /api/auth/me` - Get current user info

### Analysis
- `POST /api/analyze` - Upload CSV and get analysis (requires authentication)

## Environment Variables

Create a `.env` file in the backend directory:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///./event_summarizer.db
```

## Production Deployment

### Backend
1. Use a production ASGI server like Gunicorn with Uvicorn workers
2. Set up a PostgreSQL database
3. Configure environment variables
4. Use a proper secret key
5. Enable HTTPS

### Frontend
1. Build the production bundle: `npm run build`
2. Serve the `dist` folder using a web server (Nginx, Apache, etc.)
3. Configure API proxy if needed

## Future Improvements

- [ ] Add more ML models for better summarization
- [ ] Implement topic modeling
- [ ] Add user dashboard with history
- [ ] Support multiple file formats
- [ ] Add email notifications
- [ ] Implement rate limiting
- [ ] Add caching for better performance
- [ ] Support for larger CSV files with pagination
- [ ] Real-time analysis progress updates
- [ ] Export to PDF format

## License

MIT License

## Contributors

Team EVLENS
