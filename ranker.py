from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def boost_with_keywords(resume_texts, jd_text, base_scores):
    important_keywords = ["python", "flask", "ml", "machine learning", "nlp", "data", "sql"]
    keyword_weight = 0.2  
    boosts = []
    for text in resume_texts:
        count = sum(1 for kw in important_keywords if kw in text)
        boosts.append(count * keyword_weight)

    boosted_scores = [min(score + boost, 1.0) for score, boost in zip(base_scores, boosts)]
    return boosted_scores


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

    base_scores = scores.ravel()
    final_scores = boost_with_keywords(resume_texts, job_desc_text, base_scores)
    return final_scores
