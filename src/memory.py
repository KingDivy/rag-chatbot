from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from app import llm

memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True   
)