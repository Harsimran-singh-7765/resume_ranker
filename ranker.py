from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(resume_texts, job_desc_text):
    """
    Compares each resume against the job description using TF-IDF + cosine similarity.
    Returns a list of match scores (float values).
    """

    all_texts = resume_texts + [job_desc_text]

  
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)


    jd_vector = tfidf_matrix[-1]
    resume_vectors = tfidf_matrix[:-1]  

    
    scores = cosine_similarity(resume_vectors, jd_vector)

    return scores.ravel()  