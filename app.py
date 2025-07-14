import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from pdf_extractor import extract_text_from_pdf
from text_cleaner import preprocess
from ranker import rank_resumes

# Flask App Setup
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    ranks = []

    if request.method == 'POST':
        # Get Job Description from form
        jd_text = request.form['jd']
        jd_cleaned = preprocess(jd_text)

        resumes = request.files.getlist("resumes")
        resume_texts = []
        resume_names = []

        for resume in resumes:
            filename = secure_filename(resume.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            resume.save(save_path)

            extracted_text = extract_text_from_pdf(save_path)
            cleaned_text = preprocess(extracted_text)

            resume_texts.append(cleaned_text)
            resume_names.append(filename)

        # Score resumes
        scores = rank_resumes(resume_texts, jd_cleaned)

        # Pair names with scores and sort
        ranks = sorted(zip(resume_names, scores), key=lambda x: x[1], reverse=True)

    return render_template("index.html", ranks=ranks)

# Run app
if __name__ == '__main__':
    app.run(debug=True)
