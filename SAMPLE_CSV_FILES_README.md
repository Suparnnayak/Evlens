# Sample CSV Files for Testing

I've created three sample CSV files that you can use to test the Event Review Summarizer application:

## 📁 Available Files

### 1. `sample_event_reviews.csv` (Recommended)
- **20 event reviews** with varied content
- Mix of positive, neutral, and slightly negative reviews
- Good for comprehensive testing
- Reviews cover different event types: TechFest, MusicFest, Hackathon, Conference, Workshop, etc.

### 2. `sample_event_reviews_small.csv` (Quick Test)
- **5 event reviews** for quick testing
- Smaller file size for faster processing
- Good for initial testing and debugging
- Perfect if you want to test the flow quickly

### 3. `sample_event_reviews_mixed_sentiment.csv` (Sentiment Testing)
- **20 event reviews** with **strongly varied sentiment**
- Includes very positive, very negative, and neutral reviews
- Best for testing sentiment analysis features
- Will show clear differences in sentiment classification

## 📋 CSV Format

All files follow this format:
```csv
event_name,review_text
Event Name,"Review text here..."
```

## 🚀 How to Use

1. **Start your backend and frontend servers** (if not already running)
2. **Login** to the application at `http://localhost:3000`
3. **Navigate to the Dashboard**
4. **Click "Upload CSV"** or the file upload area
5. **Select one of the sample CSV files**
6. **Click "Analyze Reviews"**
7. **View the results**: Summary, sentiment analysis, and insights

## 💡 Testing Tips

- Start with `sample_event_reviews_small.csv` for a quick test
- Use `sample_event_reviews_mixed_sentiment.csv` to see how sentiment analysis works with varied reviews
- Use `sample_event_reviews.csv` for a comprehensive test with realistic data

## 📊 Expected Results

After uploading and analyzing:
- **Summary**: AI-generated summary of all reviews
- **Sentiment Analysis**: Breakdown of positive, neutral, and negative reviews
- **Key Insights**: Automatically extracted insights from the reviews
- **Download**: Option to download results as JSON

## 🔧 Troubleshooting

If you encounter any issues:
- Make sure the CSV file has the correct format (event_name, review_text columns)
- Check that the backend server is running
- Verify the file is a valid CSV (no encoding issues)
- Check the browser console for any errors

---

**Note**: These are sample files created for testing purposes. Feel free to modify them or create your own CSV files following the same format!

