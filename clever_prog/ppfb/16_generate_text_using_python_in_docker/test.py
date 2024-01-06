from transformers import pipeline

model = pipeline("text-generation", model="gpt2")

sentences = model("Hi, My name is John Cena, I am here",
                  do_sample=True, top_k=50,
                  temperature=0.9, max_length=100,
                  num_return_sequences=2)

for sentence in sentences:
    print(sentence["generated_text"])