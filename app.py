from flask import Flask, render_template, request

from src.helper import load_pdf_file, filter_short_documents, text_spliting
from src.store_index import download_embeddings, store_index
from src.prompt import prompt

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

import os

app = Flask(__name__)

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

chat_history = []


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0
)


extracted_doc = load_pdf_file("data")

filtered_docs = filter_short_documents(extracted_doc)

text_chunks = text_spliting(filtered_docs)

embedding = download_embeddings()

index_name = "companylaw-chatbot"

docstore = store_index(text_chunks, embedding, index_name)

retriever = docstore.as_retriever()

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

@app.route("/")
def home():
    return render_template("index.html", chat_history=chat_history)


@app.route("/chat", methods=["POST"])     
def chat():
    user_question = request.form["question"]

    chat_history.append({"role": "user", "text": user_question})

    response = rag_chain.invoke(user_question)

    # Save bot message
    chat_history.append({"role": "bot", "text": response})

    return render_template(
        "index.html",
        question=user_question,
        answer=response,
        chat_history=chat_history
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
