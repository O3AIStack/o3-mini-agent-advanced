import openai
import os
from src.utils import load_prompt_template

openai.api_key = os.getenv("OPENAI_API_KEY")

def evaluate_summary(summary: str) -> str:
    template = load_prompt_template("evaluator.txt")
    prompt = template.replace("{{SUMMARY}}", summary)

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()
