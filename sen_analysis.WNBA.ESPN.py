# sentiment_sports_titles.py

import pandas as pd
from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze sentiment of a text and return sentiment category and polarity.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive "
    elif polarity < 0:
        sentiment = "Negative "
    else:
        sentiment = "Neutral "
    return sentiment, polarity

def main():
    # Load CSV file
    # The CSV should have a column named 'title'
    filename = input("Enter the CSV filename (with .csv): ")
    df = pd.read_csv(filename)

    # Check if 'title' column exists
    if 'Title' not in df.columns:
        print("CSV must contain a 'title' column.")
        return

    # Analyze sentiment for each title
    sentiments = []
    polarities = []

    for title in df['Title']:
        sentiment, polarity = analyze_sentiment(title)
        sentiments.append(sentiment)
        polarities.append(polarity)

    # Add results to the DataFrame
    df['Sentiment'] = sentiments
    df['Polarity'] = polarities

    # Save results to a new CSV
    output_filename = "WNBA_espn_sentiment.csv"
    df.to_csv(output_filename, index=False)
    print(f"Sentiment analysis complete. Results saved to '{output_filename}'.")

if __name__ == "__main__":
    main()
