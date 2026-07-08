from src.parser.resume_parser import parse_resume
from src.nlp.similarity import calculate_similarity
from src.llm.evaluator import evaluate_resume
from src.scoring.scorer import calculate_final_score


def process_resume(job_description: str, resume_path: str):

    parsed_resume = parse_resume(resume_path)

    similarity_score = calculate_similarity(
        job_description,
        parsed_resume["text"]
    )

    llm_result = evaluate_resume(
        job_description,
        parsed_resume["text"]
    )

    final_score = calculate_final_score(
        similarity_score,
        llm_result["score"]
    )

    return {
        "candidate": parsed_resume["filename"],
        "similarity_score": similarity_score,
        "llm_score": llm_result["score"],
        "final_score": final_score,
        "matched_skills": llm_result["matched_skills"],
        "missing_skills": llm_result["missing_skills"],
        "strengths": llm_result["strengths"],
        "weaknesses": llm_result["weaknesses"],
        "recommendation": llm_result["recommendation"],
        "reason": llm_result["reason"]
    }