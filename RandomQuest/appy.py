from flask import Flask, render_template, request, jsonify
import PyPDF2
import requests

app = Flask(__name__)


GEMINI_QUESTION_API = 'https://gemini-api.example.com/generate_question'  # Replace with actual URL
GEMINI_VERIFY_API = 'https://gemini-api.example.com/verify_answer'  # Replace with actual URL

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['pdf']
    pdf_text = extract_text_from_pdf(file)

    # Sending the extracted text to Gemini API to generate a question
    response = requests.post(GEMINI_QUESTION_API, json={'content': pdf_text})
    if response.status_code == 200:
        question = response.json().get('question')
        return jsonify({'question': question})
    else:
        return jsonify({'error': 'Failed to generate question'}), 500

@app.route('/verify', methods=['POST'])
def verify_answer():
    answer = request.form.get('answer')
    pdf_text = request.form.get('pdf_text')

    # Sending the answer and PDF text to Gemini API for verification
    response = requests.post(GEMINI_VERIFY_API, json={'content': pdf_text, 'answer': answer})
    if response.status_code == 200:
        is_correct = response.json().get('is_correct')
        return jsonify({'is_correct': is_correct})
    else:
        return jsonify({'error': 'Failed to verify answer'}), 500

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    return text

if __name__ == '__main__':
    app.run(debug=True)
