from src.nlp.similarity import calculate_similarity

jd = """
Python Developer

Skills:

Python
Machine Learning
SQL
TensorFlow
Git
"""

resume = """
Python Developer

Skills

Python
SQL
Git

Worked on Machine Learning projects using Scikit-learn.
"""

score = calculate_similarity(jd, resume)

print("Similarity Score:", score)