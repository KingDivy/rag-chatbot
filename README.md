# 📘 RAG Chatbot – Flask • LangChain • Gemini • Docker • AWS

An end-to-end **Retrieval-Augmented Generation (RAG) chatbot** built using **Flask**, **LangChain**, **Google Gemini**, and **HuggingFace embeddings**, deployed with **Docker** on **AWS (ECR + EC2)**.

This chatbot allows users to ask questions based on uploaded PDF documents and receive accurate, context-aware answers.

---

## 🚀 Features

- 📄 PDF document ingestion  
- 🔍 Semantic search using vector embeddings  
- 🧠 Context-aware answers using RAG  
- 💬 Conversational memory support  
- 🎨 Clean and modern chat UI  
- 🐳 Dockerized application  
- ☁️ CI/CD pipeline using GitHub Actions  
- 🚀 Deployment on AWS EC2 via Amazon ECR  

---

## 🛠️ Tech Stack

**Backend**
- Python
- Flask
- LangChain
- Google Gemini API
- HuggingFace Embeddings

**Frontend**
- HTML
- CSS
- Jinja2

**DevOps**
- Docker
- GitHub Actions
- AWS EC2
- Amazon ECR

---

## 📂 Project Structure

```
rag-chatbot/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── setup.py
│
├── data/
│
├── src/
│   ├── helper.py
│   ├── store_index.py
│   ├── prompt.py
│   ├── memory.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── research/
│   └── trials.ipynb
│
└── .github/workflows/
    └── cicd.yaml
```

---

## ⚙️ Local Setup

### 1. Clone Repository

```bash
git clone https://github.com/KingDivy/rag-chatbot.git
cd rag-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

### 4. Run Application

```bash
python app.py
```

Open:

```
http://localhost:5000
```

---

## 🐳 Docker Usage

### Build Image

```bash
docker build -t rag-chatbot .
```

### Run Container

```bash
docker run -d -p 5000:5000 rag-chatbot
```

---

## ☁️ AWS Deployment

- Docker image is pushed to **Amazon ECR**
- EC2 pulls and runs the container
- CI/CD automated via GitHub Actions

Ensure:
- Port **5000** allowed in EC2 Security Group
- Flask runs with `host="0.0.0.0"`

```python
app.run(host="0.0.0.0", port=5000)
```

---

## 🔄 CI/CD

- Triggered on push to `main`
- Builds Docker image
- Pushes image to ECR
- Deploys to EC2

Workflow file:

```
.github/workflows/cicd.yaml
```

---

## 👤 Author

**Divy Desai**  
GitHub: [@KingDivy](https://github.com/KingDivy)

---

## 📄 License

This project is licensed under the **Apache License 2.0**.

You may obtain a copy of the License at:

```
http://www.apache.org/licenses/LICENSE-2.0
```

Unless required by applicable law or agreed to in writing, software  
distributed under the License is distributed on an **"AS IS" BASIS**,  
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.

---
