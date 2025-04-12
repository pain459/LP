import subprocess
from scripts.chat_manager import save_chat, get_chats

MODEL_PATH = "model/llama-2-7b.Q4_K_M.gguf"  # Adjust your actual model file name
LLAMA_CMD = ["./llama.cpp/main", "-m", MODEL_PATH, "-p"]

def chat():
    print("LLM CLI is live. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        try:
            result = subprocess.run(
                LLAMA_CMD + [user_input],
                cwd="llama.cpp",
                capture_output=True,
                text=True
            )
            output = result.stdout.strip()
            print(f"LLM: {output}")
            save_chat(user_input, output)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat()
