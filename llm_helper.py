from langchain_groq import ChatGroq
from config import settings

llm = ChatGroq(
    groq_api_key = settings.GROQ_API_KEY, 
    model_name = "openai/gpt-oss-120b"
    )

if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)