import os
import tiktoken

def load_prompt_template(filename: str) -> str:
    path = os.path.join("prompts", filename)
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def count_tokens(text: str, model: str = "gpt-4-turbo") -> int:
    try:
        enc = tiktoken.encoding_for_model(model)
    except KeyError:
        enc = tiktoken.get_encoding("cl100k_base")  # fallback

    return len(enc.encode(text))
