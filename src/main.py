from fastapi import FastAPI, Request
from dotenv import load_dotenv
from src.logic.summarize import summarize_text
from src.logic.evaluator import evaluate_summary
from src.memory import SessionMemory
from src.utils import count_tokens
import os

load_dotenv()

app = FastAPI()
memory_store = SessionMemory()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/agent")
async def agent_endpoint(request: Request):
    body = await request.json()
    user_input = body.get("text", "")
    session_id = body.get("session_id", "default")

    # Store input in session memory
    memory_store.add_to_session(session_id, "user_input", user_input)

    # Step 1: Summarization
    summary = summarize_text(user_input)
    memory_store.add_to_session(session_id, "summary", summary)

    # Step 2: Evaluation
    evaluation = evaluate_summary(summary)
    memory_store.add_to_session(session_id, "evaluation", evaluation)

    # Token logging (optional)
    tokens_input = count_tokens(user_input)
    tokens_summary = count_tokens(summary)
    tokens_eval = count_tokens(evaluation)

    return {
        "summary": summary,
        "evaluation": evaluation,
        "token_log": {
            "input_tokens": tokens_input,
            "summary_tokens": tokens_summary,
            "evaluation_tokens": tokens_eval
        }
    }
