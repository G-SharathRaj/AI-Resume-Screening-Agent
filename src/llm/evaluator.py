import json

from src.llm.groq_client import ask_llm
from src.llm.prompts import RESUME_EVALUATION_PROMPT


def evaluate_resume(job_description: str, resume: str):

    user_prompt = f"""
JOB DESCRIPTION

{job_description}


RESUME

{resume}
"""

    response = ask_llm(
        RESUME_EVALUATION_PROMPT,
        user_prompt
    )

    # ---------- Clean LLM Output ----------
    response = response.strip()

    if response.startswith("```json"):
        response = response.replace("```json", "")

    if response.startswith("```"):
        response = response.replace("```", "")

    if response.endswith("```"):
        response = response.replace("```", "")

    response = response.strip()

    # ---------- Debug ----------
    print("\n===== LLM RESPONSE =====")
    print(response)
    print("========================\n")

    return json.loads(response)