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

    return json.loads(response)