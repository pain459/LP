from transformers import pipeline
import sys

model = pipeline("text-generation", model="gpt2")

if len(sys.argv) < 2:
    print("Please provide a statement as an argument.")
    sys.exit(1)

user_input = " ".join(sys.argv[1:])

sentences = model(user_input,
                  do_sample=True, top_k=50,
                  temperature=0.9, max_length=100,
                  num_return_sequences=2)

for sentence in sentences:
    print(sentence["generated_text"])