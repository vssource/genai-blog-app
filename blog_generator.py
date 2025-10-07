import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()
# Load system prompt from file
def load_system_prompt():
    with open("prompts/system_prompt.txt", "r") as f:
        return f.read()

# Blog generation with LangChain
def generate_blog(user_prompt: str) -> str:
    #groq_api_key = os.getenv("GROQ_API_KEY")
    groq_api_key = st.secrets["GROQ_API_KEY"]
    if not groq_api_key:
        raise ValueError("Missing GROQ_API_KEY in environment variables")

    # Initialize Groq LLM
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        #groq_api_key=groq_api_key,
        temperature=0.7,
        max_tokens=2000,
    )

    # Load system prompt
    system_prompt = load_system_prompt()

    # Build prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{topic}")
    ])

    # Chain execution
    chain = prompt | llm
    response = chain.invoke({"topic": user_prompt})

    # Ensure the return value is always a string
    content = response.content
    if isinstance(content, str):
        return content
    elif isinstance(content, list):
        # Join list elements as string, handling dicts if present
        return "\n".join(
            item if isinstance(item, str) else str(item)
            for item in content
        )
    else:
        return str(content)
