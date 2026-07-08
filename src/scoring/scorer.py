def calculate_final_score(similarity_score: float, llm_score: float) -> float:
    """
    Calculate final weighted score.
    """

    final_score = (
        similarity_score * 0.6 +
        llm_score * 0.4
    )

    return round(final_score, 2)