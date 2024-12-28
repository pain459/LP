from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Load pre-trained model and tokeniser
model_name = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# input text
text = "You are very beautiful, intelligent and idiot"
inputs = tokenizer(text, return_tensors="pt")

# Get logits
outputs = model(**inputs)
logits = outputs.logits

print(logits) # Raw scores for each class