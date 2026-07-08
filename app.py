import os
import tempfile

import pandas as pd
import streamlit as st

from src.pipeline import process_resume
from src.export.csv_export import export_to_csv
from src.export.json_export import export_to_json


st.set_page_config(
    page_title="AI Resume Screening Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Screening Agent")
st.caption(
    "AI-powered Resume Screening using Resume Parsing, Semantic Similarity and Large Language Models (Groq)."
)

st.divider()

job_description = st.text_area(
    "📄 Paste Job Description",
    height=250,
    placeholder="Paste the complete Job Description here..."
)

uploaded_resumes = st.file_uploader(
    "📂 Upload Resumes",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if st.button("🚀 Analyze Candidates", type="primary"):

    if not job_description.strip():
        st.error("Please paste a Job Description.")
        st.stop()

    if not uploaded_resumes:
        st.error("Please upload at least one resume.")
        st.stop()

    results = []

    progress = st.progress(0)
    status = st.empty()

    total = len(uploaded_resumes)

    for index, uploaded_file in enumerate(uploaded_resumes):

        status.info(f"Analyzing {uploaded_file.name}...")

        suffix = os.path.splitext(uploaded_file.name)[1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
            temp_file.write(uploaded_file.getbuffer())
            temp_path = temp_file.name

        try:

            result = process_resume(
                job_description,
                temp_path
            )

            result["candidate"] = uploaded_file.name

            results.append(result)

        except Exception as e:

            st.error(f"{uploaded_file.name}: {e}")

        finally:

            if os.path.exists(temp_path):
                os.remove(temp_path)

        progress.progress((index + 1) / total)

    status.success("✅ All resumes analyzed successfully!")

    if len(results) == 0:
        st.error("No resumes could be processed.")
        st.stop()

    results = sorted(
        results,
        key=lambda x: x["final_score"],
        reverse=True
    )

    export_to_csv(results)
    export_to_json(results)

    df = pd.DataFrame(results)

    df = df.sort_values(
        by="final_score",
        ascending=False
    ).reset_index(drop=True)

    df.insert(
        0,
        "Rank",
        range(1, len(df) + 1)
    )

    st.success("🎉 Analysis Complete!")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Candidates",
            len(df)
        )

    with col2:
        st.metric(
            "Highest Score",
            f"{df.iloc[0]['final_score']:.2f}"
        )

    with col3:
        st.metric(
            "Best Candidate",
            df.iloc[0]["candidate"]
        )

    st.divider()

    st.subheader("🏆 Candidate Ranking")

    st.dataframe(
        df[
            [
                "Rank",
                "candidate",
                "similarity_score",
                "llm_score",
                "final_score",
                "recommendation"
            ]
        ],
        hide_index=True,
        use_container_width=True
    )

    st.divider()

    st.subheader("📋 Candidate Details")

    for candidate in results:

        with st.expander(
            f"🏅 {candidate['candidate']}  |  Final Score : {candidate['final_score']}"
        ):

            st.markdown("### 📌 Recommendation")
            st.success(candidate["recommendation"])

            st.markdown("### 📝 Reason")
            st.write(candidate["reason"])

            col1, col2 = st.columns(2)

            with col1:

                st.success("✅ Matched Skills")
                st.write(candidate["matched_skills"])

                st.info("💪 Strengths")
                st.write(candidate["strengths"])

            with col2:

                st.error("❌ Missing Skills")
                st.write(candidate["missing_skills"])

                st.warning("⚠ Weaknesses")
                st.write(candidate["weaknesses"])

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        with open("output/ranking.csv", "rb") as f:
            st.download_button(
                "⬇ Download CSV",
                data=f,
                file_name="ranking.csv",
                mime="text/csv"
            )

    with col2:
        with open("output/ranking.json", "rb") as f:
            st.download_button(
                "⬇ Download JSON",
                data=f,
                file_name="ranking.json",
                mime="application/json"
            )