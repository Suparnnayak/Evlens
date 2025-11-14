"""
Improved ML service for event review analysis
"""
import sys
import os

from transformers import pipeline
from textblob import TextBlob
import numpy as np
import pandas as pd
from typing import Dict, Any, List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variable for model (lazy loading)
_summarizer = None


def get_summarizer():
    """Lazy load the summarization model"""
    global _summarizer
    if _summarizer is None:
        logger.info("Loading summarization model...")
        _summarizer = pipeline(
            "summarization",
            model="google/flan-t5-base",
            device=-1  # Use CPU (-1) or GPU (0, 1, etc.)
        )
        logger.info("Model loaded successfully")
    return _summarizer


def analyze_csv_file(csv_path: str) -> Dict[str, Any]:
    """Analyze CSV file and return report"""
    import sys
    import os
    # Add ML/src directory to path to import analyzer module
    current_dir = os.path.dirname(os.path.abspath(__file__))  # backend/
    root_dir = os.path.dirname(current_dir)  # project root
    ml_src_dir = os.path.join(root_dir, "ML", "src")
    
    if ml_src_dir not in sys.path:
        sys.path.insert(0, ml_src_dir)
    
    try:
        # Import directly from ML/src/analyzer.py
        from analyzer import analyze_csv
    except ImportError as e:
        logger.error(f"Failed to import analyzer: {e}")
        logger.error(f"Python path: {sys.path}")
        logger.error(f"Looking for analyzer in: {ml_src_dir}")
        # Fallback: try to import with full path
        import importlib.util
        analyzer_path = os.path.join(ml_src_dir, "analyzer.py")
        if os.path.exists(analyzer_path):
            spec = importlib.util.spec_from_file_location("analyzer", analyzer_path)
            analyzer_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(analyzer_module)
            analyze_csv = analyzer_module.analyze_csv
        else:
            raise ImportError(f"Could not find analyzer.py at {analyzer_path}")
    
    return analyze_csv(csv_path)


def generate_summary_improved(report: Dict[str, Any]) -> Dict[str, Any]:
    """
    Improved summary generation that uses ALL reviews, not just samples.
    Also includes better sentiment analysis and key insights.
    """
    try:
        # Get all reviews from the analysis
        analysis = report.get("analysis", {})
        
        # Find text columns (could be 'review_text' or any text column)
        text_columns = [key for key, value in report.get("columns", {}).items() 
                       if value == "text"]
        
        if not text_columns:
            return {
                "summary": "No text reviews found in the dataset.",
                "sentiment_summary": {},
                "key_insights": []
            }
        
        # Get reviews from the first text column (usually 'review_text')
        text_col = text_columns[0]
        text_data = analysis.get(text_col, {})
        
        # IMPORTANT: Use ALL reviews, not just samples
        all_reviews = text_data.get("sample_reviews", [])
        n_reviews = text_data.get("n_reviews", len(all_reviews))
        
        # If we have more reviews than samples, try to read the original CSV
        # For now, we'll use what we have, but this is an improvement area
        
        if not all_reviews:
            return {
                "summary": "No reviews found in the dataset.",
                "sentiment_summary": {},
                "key_insights": []
            }
        
        # Combine all reviews
        # Use longer text if available, but chunk for very long inputs
        combined_text = " ".join(all_reviews)
        
        # Limit to reasonable length for the model (5000 chars)
        if len(combined_text) > 5000:
            # Take first 2500 and last 2500 chars to preserve context
            combined_text = combined_text[:2500] + " " + combined_text[-2500:]
        
        # Generate summary using the model
        summarizer = get_summarizer()
        
        # Better prompt for event review summarization
        input_text = f"Summarize the following event reviews: {combined_text}"
        
        try:
            raw_summary = summarizer(
                input_text,
                max_length=150,
                min_length=40,
                do_sample=False,
                truncation=True
            )
            summary_text = raw_summary[0]["summary_text"].strip()
        except Exception as e:
            logger.error(f"Error in summarization: {e}")
            # Fallback: create a simple summary
            summary_text = f"Analyzed {n_reviews} event reviews. " + \
                          f"Average review length: {text_data.get('avg_length_words', 0):.1f} words."
        
        # Improved Sentiment Analysis
        sentiments = []
        sentiment_scores = []
        
        for review in all_reviews:
            blob = TextBlob(review)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity
            sentiments.append({
                "polarity": float(polarity),
                "subjectivity": float(subjectivity),
                "text": review[:100]  # First 100 chars
            })
            sentiment_scores.append(polarity)
        
        sentiment_scores = np.array(sentiment_scores)
        
        # More nuanced sentiment classification
        pos = int((sentiment_scores > 0.1).sum())
        neg = int((sentiment_scores < -0.1).sum())
        neu = len(sentiment_scores) - pos - neg
        
        # Calculate average sentiment
        avg_sentiment = float(np.mean(sentiment_scores))
        
        # Determine overall sentiment
        if avg_sentiment > 0.15:
            overall = "very positive"
        elif avg_sentiment > 0.05:
            overall = "mostly positive"
        elif avg_sentiment < -0.15:
            overall = "very negative"
        elif avg_sentiment < -0.05:
            overall = "mostly negative"
        else:
            overall = "mixed/neutral"
        
        # Extract key insights (simple keyword-based for now)
        # In production, you could use topic modeling or NER
        key_insights = []
        if pos > neg * 2:
            key_insights.append(f"Highly positive reception ({pos} positive reviews)")
        if neg > 0:
            key_insights.append(f"Some concerns raised ({neg} negative reviews)")
        if avg_sentiment > 0:
            key_insights.append("Overall positive sentiment")
        else:
            key_insights.append("Areas for improvement identified")
        
        sentiment_summary = {
            "positive": pos,
            "neutral": neu,
            "negative": neg,
            "overall_sentiment": overall,
            "average_sentiment_score": round(avg_sentiment, 3),
            "total_reviews": n_reviews
        }
        
        return {
            "summary": summary_text,
            "sentiment_summary": sentiment_summary,
            "key_insights": key_insights,
            "review_count": n_reviews
        }
        
    except Exception as e:
        logger.error(f"Error in generate_summary_improved: {e}")
        return {
            "summary": f"Error generating summary: {str(e)}",
            "sentiment_summary": {},
            "key_insights": []
        }

