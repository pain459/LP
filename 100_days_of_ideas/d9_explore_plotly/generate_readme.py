import os
import sys
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# -----------------------------
# Configuration
# -----------------------------
MODEL_NAME = "bigcode/starcoderbase"  # Example: a smaller StarCoder model
SOURCE_DIR = "."              # Directory containing your Python scripts
OUTPUT_FILE = "README.md"

# Prompt template for summarization
PROMPT_TEMPLATE = """
You are a code analysis assistant. I will provide you with the content of a Python script.
Your task:
1. Summarize the purpose and functionality of the script in a few sentences.
2. List and describe the main functions or classes (if any) found in the script.
3. Suggest a possible usage example (if you can infer one).

Be concise and informative.

Here is the script content:

Please produce the summary now:
"""

# -----------------------------
# Helper Functions
# -----------------------------
def load_model(model_name: str):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
    return tokenizer, model

def generate_summary(tokenizer, model, code: str, max_new_tokens=512, temperature=0.2):
    prompt = PROMPT_TEMPLATE.format(script_code=code)
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=0.9,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

    # Decode and split off the prompt
    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Try to remove the prompt from the start, leaving just the answer:
    if prompt in output_text:
        output_text = output_text.split(prompt)[-1].strip()
    return output_text

def main():
    from transformers import AutoModelForCausalLM, AutoTokenizer
    model_name = "bigcode/starcoder"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
    if not os.path.isdir(SOURCE_DIR):
        print(f"Source directory {SOURCE_DIR} does not exist.", file=sys.stderr)
        sys.exit(1)

    tokenizer, model = load_model(MODEL_NAME)

    # Collect summaries
    summaries = []
    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith(".py"):
            filepath = os.path.join(SOURCE_DIR, filename)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                code = f.read()

            # Optionally truncate code if it's very large:
            # code = code[:2000]  # just an example if needed
            
            summary = generate_summary(tokenizer, model, code)
            summaries.append((filename, summary))

    # Write README
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as readme:
        readme.write("# Project Scripts Documentation\n\n")
        for fname, summ in summaries:
            readme.write(f"## {fname}\n\n")
            readme.write(f"{summ}\n\n")

    print(f"README generated at {OUTPUT_FILE}.")

if __name__ == "__main__":
    main()
