import os
import openai
from langchain.chat_models import ChatOpenAI
from langchain.globals import set_llm_cache
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.environ["OPENAI_API_KEY"]

llm = ChatOpenAI()

from langchain.schema import(
    SystemMessage, 
    AIMessage,
    HumanMessage
)

from langchain.cache import SQLiteCache
set_llm_cache(SQLiteCache(database_path='.langchain.db'))

def get_summary(title):
    messages = [
        SystemMessage(content = "Anda menjalankan sebuah toko buku dan harus memberikan ringkasan yang sangat ringkas tentang sebuah buku yang judulnya diberikan oleh pengguna. Silakan gunakan Bahasa Indonesia"),
        HumanMessage(content=title)
    ]
    output = llm.invoke(messages)
    return output.content


def get_recommendation(title):
    messages = [
        SystemMessage(content = "Berdasarkan judul yang diberikan oleh pengguna, harap berikan 3 rekomendasi buku serupa."),
        HumanMessage(content = title)
    ]
    output = llm.invoke(messages)
    return output.content
