from src.scoring.scorer import calculate_final_score


def rank_candidates(results: list):

    ranked = []

    for candidate in results:

        similarity = candidate["similarity_score"]
        llm = candidate["llm_score"]

        candidate["final_score"] = calculate_final_score(
            similarity,
            llm
        )

        ranked.append(candidate)

    ranked.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return ranked