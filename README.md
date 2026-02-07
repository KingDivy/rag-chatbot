# RAG Chatbot – Flask • LangChain • Gemini • Docker • AWS

An end-to-end Retrieval-Augmented Generation (RAG) chatbot built using Flask, LangChain, Google Gemini, and HuggingFace embeddings, deployed using Docker and AWS (ECR + EC2).

This chatbot allows users to ask questions based on uploaded PDF documents and get accurate, context-aware answers.

🚀 Features

📄 PDF document ingestion

🔍 Semantic search using vector embeddings

🧠 Context-aware answers using RAG

💬 Conversational memory support

🎨 Clean and modern chat UI

🐳 Dockerized application

☁️ CI/CD pipeline using GitHub Actions

🚀 Deployment on AWS EC2 via Amazon ECR

🛠️ Tech Stack

Backend

Python

Flask

LangChain

Google Gemini API

HuggingFace Embeddings

Pinecone / Vector Store (if enabled)

Frontend

HTML

CSS (custom modern UI)

Jinja2 Templates

DevOps

Docker

GitHub Actions (CI/CD)

AWS EC2

Amazon ECR

📂 Project Structure
rag-chatbot/
│
├── app.py                  # Flask app entry point
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── setup.py
│
├── data/                   # PDF documents
│
├── src/
│   ├── helper.py           # PDF loading & preprocessing
│   ├── store_index.py      # Vector store & embeddings
│   ├── prompt.py           # Prompt templates
│   ├── memory.py           # Conversation memory
│
├── templates/
│   └── index.html          # Chat UI
│
├── static/
│   └── style.css           # Styling
│
├── research/
│   └── trials.ipynb        # Experimentation notebook
│
└── .github/workflows/
    └── cicd.yaml           # CI/CD pipeline

⚙️ Installation & Setup (Local)
1️⃣ Clone the Repository
git clone https://github.com/KingDivy/rag-chatbot.git
cd rag-chatbot

2️⃣ Create Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Environment Variables

Create a .env file:

GOOGLE_API_KEY=your_gemini_api_key

5️⃣ Run the App
python app.py


Open browser:

http://localhost:5000

🐳 Docker Setup
Build Image
docker build -t rag-chatbot .

Run Container
docker run -d -p 5000:5000 rag-chatbot


Access:

http://localhost:5000

☁️ AWS Deployment (EC2 + ECR)

Docker image is built and pushed to Amazon ECR

EC2 pulls the image and runs the container

CI/CD automated using GitHub Actions

Ensure:

EC2 security group allows port 5000 (or 80)

Flask runs with host="0.0.0.0"

app.run(host="0.0.0.0", port=5000)

🔄 CI/CD Pipeline

Triggered on every push to main:

Build Docker image

Push image to Amazon ECR

Deploy container on EC2

Workflow file:

.github/workflows/cicd.yaml

📸 Screenshots

(Add UI screenshots here once ready)

🧠 Future Improvements

🔐 Authentication

📤 File upload via UI

📊 Chat history persistence

🌍 Multi-document support

⚡ Streaming responses

👤 Author

Divy Desai
GitHub: @KingDivy

📄 License

This project is licensed under the MIT License.
