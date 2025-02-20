from transformers import pipeline
import sys

def classify_sentiment(text):
    classifier = pipeline('sentiment-analysis')
    result = classifier(text)
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py \"Tu texto aquí\"")
        sys.exit(1)
    
    text = sys.argv[1]
    sentiment = classify_sentiment(text)
    print(sentiment)
