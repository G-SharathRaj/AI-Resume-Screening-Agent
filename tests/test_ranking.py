from src.scoring.ranking import rank_candidates

results = [

    {
        "candidate": "Alice",
        "similarity_score": 84,
        "llm_score": 90
    },

    {
        "candidate": "Bob",
        "similarity_score": 92,
        "llm_score": 70
    },

    {
        "candidate": "Charlie",
        "similarity_score": 75,
        "llm_score": 95
    }

]

ranking = rank_candidates(results)

for candidate in ranking:
    print(candidate)