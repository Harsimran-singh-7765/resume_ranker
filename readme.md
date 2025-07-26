# Resume Ranker – AI/ML Internship Project

**Internship at:** ElevateLabs  
**Intern:** Harsimran Singh  
**Project:** Resume Ranker – An intelligent resume matching system using NLP  

---

##  Project Summary

During my AI/ML internship at **ElevateLabs**, I developed a **Resume Ranker**, a web-based tool that intelligently evaluates and ranks multiple resumes against a given job description. The goal was to simplify and improve the shortlisting process in hiring by using Natural Language Processing (NLP) techniques.

The project combines **TF-IDF (Term Frequency-Inverse Document Frequency)** with **cosine similarity** to measure textual relevance. Additionally, I implemented a custom **keyword boosting mechanism** to prioritize resumes that contain important skills related to the job domain (like Python, ML, SQL, etc.).

The entire solution is wrapped in a lightweight web interface using **Flask**, making it user-friendly and easy to test or deploy.

---

##  Key Features

- Upload or input **multiple resumes** and a **job description**
- Automatically compares and scores each resume's similarity with the job description
- Boosts scores for resumes containing **key AI/ML-related keywords**
- Clean web interface using **Flask**, usable from browser
- Score output ranges from **0.0 to 1.0**, helping identify the best matches quickly

---

##  Tech Stack

| Component         | Technology Used             |
|------------------|-----------------------------|
| Programming Lang | Python                      |
| NLP Methods      | TF-IDF, Cosine Similarity   |
| UI Framework     | Flask (Python micro web framework) |
| Data Processing  | scikit-learn                |

---

##  Project Approach

1. **Text Vectorization:**  
   All resume texts and the job description are converted into vector form using TF-IDF, allowing comparison based on word frequency patterns.

2. **Similarity Measurement:**  
   Cosine similarity is used to compute how close each resume is to the job description in vector space.

3. **Keyword-Based Boosting:**  
   To enhance relevance, certain key technical terms (e.g., "python", "machine learning", "sql") are used to boost scores of resumes that mention them.

4. **Result Display:**  
   The ranked results are displayed on a simple Flask-powered web interface showing match scores for each resume.

---

##  Outcomes

- Applied key NLP techniques in a practical, real-world scenario.
- Built an end-to-end ML/NLP pipeline with user interaction.
- Understood the importance of domain-specific boosting in text similarity tasks.
- Delivered a working prototype that could be expanded into a recruitment tool.

---

##  Possible Future Enhancements

- Add support for uploading resumes in PDF/Word formats and parsing them.
- Use more advanced embeddings (like BERT or sentence transformers) for better accuracy.
- Integrate a feedback system to explain why each resume was ranked a certain way.
- Host the app online via Render or Streamlit for easier access.

---

## 👨 Author

**Harsimran Singh**  
AI/ML Intern – ElevateLabs  
 [your.email@example.com]  
🔗 [LinkedIn or GitHub profile if you want]

---

##  Final Notes

This project represents my growing experience in the field of Machine Learning, NLP, and practical software development. I learned how to take a problem from idea to implementation, with clean logic and user-facing features. Special thanks to the team at **ElevateLabs** for the opportunity!

