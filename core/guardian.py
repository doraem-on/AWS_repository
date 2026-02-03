import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate


load_dotenv()

# 2. i am initializing gemini model here
# We re use 'temperature=0' because we want the AI to be factual/strict, not creative.
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

def analyze_compliance(text_content):
    """
    Analyzes text for safety, bias, and legal risks.
    """
    
    # 3. The Prompt Template ....
    # We  re use {text} as a placeholder for whatever the user uploads.
    template = """
    You are a Senior Compliance Officer for a large media company in India.
    Analyze the following script for:
    1. Legal Risks (e.g., false financial promises, hate speech).
    2. Brand Safety (e.g., controversial political opinions).
    3. Cultural Insensitivity.

    Script: "{text}"

    If the script is SAFE, return exactly: "SAFE".
    If the script is RISKY, return a bulleted list of issues and a suggested rewrite.
    """

    prompt = PromptTemplate(template=template, input_variables=["text"])

    # 4. The Chain ....
    # This sends the instructions + user text to Gemini.
    chain = prompt | llm
    
    response = chain.invoke({"text": text_content})
    return response.content