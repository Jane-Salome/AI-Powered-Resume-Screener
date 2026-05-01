# AI-Powered Resume Screener (TF-IDF + Cosine Similarity + Streamlit UI)

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PyPDF2 import PdfReader
import docx2txt
import plotly.express as px

# ------------------- Helper Functions ------------------- #

def extract_text_from_pdf(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        return ""

def extract_text_from_docx(docx_file):
    try:
        text = docx2txt.process(docx_file)
        return text.strip()
    except Exception as e:
        return ""

def read_resume(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)
    else:
        return ""

def compute_similarity(resume_texts, job_description):
    corpus = resume_texts + [job_description]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)
    job_vec = tfidf_matrix[-1]
    resume_vecs = tfidf_matrix[:-1]
    scores = cosine_similarity(resume_vecs, job_vec)
    return scores.flatten()

# ------------------- Streamlit UI ------------------- #

st.set_page_config(page_title="AI Resume Screener", layout="wide")
st.title("📄 AI-Powered Resume Screener")
st.write("Automatically rank and score candidate resumes against a job description using TF-IDF and Cosine Similarity.")

# Sidebar
st.sidebar.markdown("### 📄 AI Resume Screener")

# Upload Job Description
st.sidebar.header("Job Description")
jd_file = st.sidebar.text_area("Paste Job Description Here")

# Upload Resumes
st.sidebar.header("Upload Resumes")
resume_files = st.sidebar.file_uploader("Upload Multiple Resumes (PDF/DOCX)", type=['pdf', 'docx'], accept_multiple_files=True)

# Screening Button
if st.sidebar.button("⚙️ Run Screening"):
    if not jd_file or not resume_files:
        st.warning("Please provide both a job description and at least one resume.")
    else:
        st.info("🔍 Screening resumes... Please wait.")
        resume_texts = []
        candidate_names = []

        for file in resume_files:
            text = read_resume(file)
            if text:
                resume_texts.append(text)
                candidate_names.append(file.name)
            else:
                resume_texts.append("")
                candidate_names.append(file.name + " (Error Reading File)")

        scores = compute_similarity(resume_texts, jd_file)

        results_df = pd.DataFrame({
            'Candidate Name': candidate_names,
            'Match Score (%)': np.round(scores * 100, 2)
        }).sort_values(by='Match Score (%)', ascending=False).reset_index(drop=True)

        results_df["Candidate Name"] = results_df["Candidate Name"].str.replace(r"\.(pdf|docx)$", "", regex=True)

        st.success("✅ Screening complete!")

        st.subheader("📊 Candidate Match Table")
        st.dataframe(results_df)

        st.subheader("🏆 Candidate Ranking")
        fig = px.bar(
            results_df,
            x="Match Score (%)",
            y="Candidate Name",
            orientation="h",
            text="Match Score (%)",
            title="Candidate Ranking by Match Score",
            color="Match Score (%)",
            color_continuous_scale="Blues"
        )
        fig.update_traces(textposition="outside")
        fig.update_layout(
            yaxis=dict(autorange="reversed"),
            margin=dict(l=150)
        )
        st.plotly_chart(fig, use_container_width=True)

        st.download_button(
            "📥 Download Results (CSV)",
            data=results_df.to_csv(index=False),
            file_name="resume_scores.csv",
            mime="text/csv"
        )

        img_bytes = fig.to_image(format="png", width=900, height=600, scale=2)
        st.download_button(
            label="⬇️ Download Ranking Chart (PNG)",
            data=img_bytes,
            file_name="candidate_ranking.png",
            mime="image/png"
        )

# Footer
st.markdown("---")
st.markdown("### About the Developer")
st.markdown("**Jane Salome D**")
st.markdown("""
B.Tech Information Technology — Sri Sairam Engineering College

🔗 [LinkedIn](https://www.linkedin.com/in/jane-salome-d-a47a91295)  
💻 [GitHub](https://github.com/Jane-Salome)  
📧 janesalome4@gmail.com
""")
