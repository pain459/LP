from transformers import pipeline

print("Sentimental analysis program.")
classifier = pipeline("Sentimental analysis")
classifier("The existence of micro organisms proves that universe is infinite. Its just we are unable to see it yet.")


