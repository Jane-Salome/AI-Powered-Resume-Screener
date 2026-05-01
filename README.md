# AI-Powered Resume Screener 📄

**Live Demo** → [Click here to view the app](https://ai-powered-resume-screener-rtenigffmpazvvnapttnib.streamlit.app/)

An intelligent resume screening tool that automatically ranks candidate resumes against a job description using TF-IDF vectorization and Cosine Similarity — helping recruiters shortlist the best candidates instantly without manual scanning.

---

## Features

- **Multi-format Resume Upload** — Supports both PDF and DOCX resume formats
- **Job Description Matching** — Paste any job description and instantly rank all uploaded resumes
- **TF-IDF + Cosine Similarity** — Ranks resumes based on keyword relevance to the job description
- **Ranked Results Table** — Displays candidates sorted by match score (%)
- **Visual Bar Chart** — Interactive Plotly chart showing candidate rankings
- **CSV Export** — Download ranked results for further review
- **Chart Download** — Export candidate ranking chart as PNG
- **Interactive UI** — Built entirely with Streamlit

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python |
| Frontend | Streamlit |
| PDF Parsing | PyPDF2 |
| DOCX Parsing | docx2txt |
| ML / NLP | scikit-learn (TF-IDF + Cosine Similarity) |
| Data Handling | pandas, numpy |
| Visualization | Plotly |

---

## How It Works

1. **Upload Resumes** — Upload one or more resumes (PDF or DOCX) via the sidebar
2. **Paste Job Description** — Enter the job description text in the sidebar
3. **Text Extraction** — PyPDF2 and docx2txt extract raw text from each resume
4. **TF-IDF Vectorization** — All resume texts and the job description are converted into TF-IDF vectors
5. **Cosine Similarity** — Similarity score between each resume and the job description is computed
6. **Ranking** — Candidates are ranked by match score from highest to lowest
7. **Results** — View ranked table, interactive chart, and download results as CSV

---

## Getting Started

### Prerequisites
Python 3.8+

### Installation

```bash
# Clone the repository
git clone https://github.com/Jane-Salome/AI-Powered-Resume-Screener.git
cd AI-Powered-Resume-Screener

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## Requirements

```
streamlit
pandas
numpy
scikit-learn
PyPDF2
docx2txt
plotly
kaleido
```

---

## Project Structure

```
├── app.py                # Main Streamlit application
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## Example Use Case

Imagine you're hiring a **Software Engineer**. Paste the job description, upload 10 resumes, and instantly see which candidates best match — saving hours of manual review.

---

## Future Improvements

- Upgrade from TF-IDF to transformer embeddings (BERT / Sentence-BERT) for semantic matching
- Add ATS scoring based on resume formatting and section detection
- Support bulk screening with progress tracking

---

## Author

**Jane Salome D**  
B.Tech Information Technology — Sri Sairam Engineering College  
[LinkedIn](https://www.linkedin.com/in/jane-salome-d-a47a91295) | [GitHub](https://github.com/Jane-Salome)
