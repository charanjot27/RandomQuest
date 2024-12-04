AI-Powered Question-Answer Validation System
This project is a Flask-based web application designed to streamline the process of creating and validating subjective answers using AI integration. The key features and functionalities of this project are as follows:

PDF Upload for Question Generation:
The system allows users to upload PDF files containing textual content.
It processes the uploaded PDF, extracts text, and uses AI algorithms to generate insightful, relevant questions based on the content.
AI-Generated Questions:
Questions are dynamically generated using advanced natural language processing (NLP) models, ensuring relevance to the uploaded document.
The system focuses on creating subjective questions that encourage deeper understanding.
Subjective Answer Submission:
Users can input their answers to the generated questions through an intuitive interface.
The answers are saved and prepared for evaluation.
Answer Verification with Gemini API:
The application integrates with the Gemini API for answer validation.
Gemini API evaluates the subjective answers based on correctness, coherence, and alignment with the uploaded document.
The system provides feedback or a score to the user, ensuring accurate and meaningful evaluations.
Flask Backend and Frontend Integration:
Flask serves as the core framework for handling backend processes, such as file uploads, text extraction, question generation, and API requests.
The frontend interface is designed to be user-friendly, supporting smooth navigation through the upload, question, and validation processes.
Use Cases:
Ideal for educators, students, or organizations aiming to create automated assessments from study materials.
Useful for enhancing learning efficiency through instant feedback on subjective answers.
Technologies Used:
Python: Core programming language for backend functionality.
Flask: Web framework for developing and deploying the application.
NLP Models: For question generation using AI.
Gemini API: For answer validation and feedback.
PDF Parsing Libraries: For extracting text from uploaded PDFs.
