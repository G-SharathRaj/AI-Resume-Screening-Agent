# 🤖 AI Resume Screening Agent

An AI-powered Resume Screening Agent that automatically analyzes and ranks candidate resumes against a Job Description using **Resume Parsing**, **Semantic Similarity**, and **Large Language Models (LLMs)**.

Built as part of a 24-hour AI Agent Challenge.

---

# 🚀 Features

✅ Parse resumes from PDF, DOCX, and TXT

✅ Semantic Resume Matching using Sentence Transformers

✅ AI-powered Resume Evaluation using Groq (Llama 3.3)

✅ Candidate Ranking based on weighted scoring

✅ Skills Gap Analysis

✅ Strengths & Weaknesses Identification

✅ AI Recommendation for each candidate

✅ CSV & JSON Export

✅ Interactive Streamlit Dashboard

---

# 🏗️ Project Architecture

```
                    User

                      │

                      ▼

         Upload Job Description

                      │

                      ▼

         Upload Multiple Resumes

                      │

                      ▼

             Resume Parser
      (PDF / DOCX / TXT)

                      │

                      ▼

      Semantic Similarity Engine
      (Sentence Transformers)

                      │

                      ▼

        Groq LLM Evaluation
      (Llama 3.3 70B Versatile)

                      │

                      ▼

        Weighted Scoring Engine

                      │

                      ▼

          Candidate Ranking

                      │

                      ▼

      CSV / JSON Export + Dashboard
```

---

# 🛠️ Tech Stack

## Programming Language

- Python 3.12

## Frontend

- Streamlit

## AI / NLP

- Groq API
- Llama 3.3 70B Versatile
- Sentence Transformers
- all-MiniLM-L6-v2

## Machine Learning

- Scikit-learn
- Cosine Similarity

## Resume Parsing

- pdfplumber
- python-docx

## Data Processing

- Pandas

---

# 📁 Project Structure

```
AI-Resume-Screening-Agent/

│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── sample_data/
│   ├── job_description.txt
│   ├── resume1.pdf
│   ├── resume2.pdf
│   └── resume3.pdf
│
├── output/
│   ├── ranking.csv
│   └── ranking.json
│
├── src/
│
│   ├── parser/
│   ├── nlp/
│   ├── llm/
│   ├── scoring/
│   ├── export/
│   └── pipeline.py
│
└── tests/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/G-SharathRaj/AI-Resume-Screening-Agent.git

cd AI-Resume-Screening-Agent
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key_here
```

Get your free API key from:

https://console.groq.com/

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📊 How It Works

1. Paste a Job Description.
2. Upload one or more resumes.
3. Click **Analyze Candidates**.
4. The application:

- Parses each resume.
- Computes semantic similarity.
- Sends the resume and JD to the LLM.
- Extracts strengths, weaknesses, and skills.
- Calculates the final score.
- Ranks all candidates.
- Exports results as CSV and JSON.

---

# 📷 Screenshots

## Home Screen

_Add screenshot here_

---

## Candidate Ranking

_Add screenshot here_

---

## Candidate Analysis

_Add screenshot here_

---

# 📈 Scoring Method

Final Score is calculated using:

```
Final Score =
60% Semantic Similarity +
40% LLM Evaluation
```

This combines objective NLP-based matching with AI reasoning for more reliable candidate evaluation.

---

# 📤 Output

The application generates:

- Candidate Ranking
- Similarity Score
- AI Evaluation Score
- Final Weighted Score
- Recommendation
- Strengths
- Weaknesses
- Matched Skills
- Missing Skills

It also exports:

- `ranking.csv`
- `ranking.json`

---

# ⚠️ Limitations

- Requires a valid Groq API Key.
- Works best with text-based resumes.
- OCR is not implemented for scanned PDFs.
- AI evaluation depends on the quality of the Job Description.

---

# 🔮 Future Improvements

- Resume OCR Support
- Batch Processing
- Recruiter Dashboard
- Authentication
- ATS Score Visualization
- Interview Question Generation
- Email Integration
- Database Support
- Docker Deployment

---

# 👨‍💻 Author

**G Sharath Raj**

GitHub

https://github.com/G-SharathRaj

LinkedIn

https://www.linkedin.com/in/sharath-raj-390626377

---

# 📜 License

This project was developed for educational purposes and an AI Agent Challenge.