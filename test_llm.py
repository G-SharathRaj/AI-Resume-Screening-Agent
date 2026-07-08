from src.llm.evaluator import evaluate_resume

jd = """
Looking for a Python Machine Learning Engineer.

Skills:
Python
SQL
Machine Learning
TensorFlow
Git
"""

resume = """
Python Developer

Skills

Python
Java
Git
SQL

Worked on Machine Learning projects using Scikit-learn.
"""

result = evaluate_resume(jd, resume)

print(result)