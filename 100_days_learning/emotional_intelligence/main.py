from transformers import pipeline

# Load pretrained sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

def analyze_emotion():
    print("Welcome to emotional intelligence demo!")
    print("Entrer a sentence or a paragraph to analyze the emotional tone:")
    text = input("-->")

    # Perform sentiment analysis
    results = classifier(text)

    print("Emotional analysis resulst:")
    for result in results:
        label = result['label']
        score = result['score']
        print(f"Sentiment: {label} (Confidence: {score:.2f})")


if __name__ == '__main__':
    analyze_emotion()