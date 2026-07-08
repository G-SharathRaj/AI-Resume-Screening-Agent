from sklearn.metrics.pairwise import cosine_similarity

from src.nlp.embeddings import get_embedding


def calculate_similarity(job_description: str, resume: str) -> float:
    """
    Calculate semantic similarity between
    a job description and a resume.

    Returns:
        Similarity percentage (0-100)
    """

    jd_embedding = get_embedding(job_description)
    resume_embedding = get_embedding(resume)

    similarity = cosine_similarity(
        [jd_embedding],
        [resume_embedding]
    )[0][0]

    return round(float(similarity * 100), 2)