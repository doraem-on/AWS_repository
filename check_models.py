import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load your API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: API Key not found. Check your .env file.")
else:
    genai.configure(api_key=api_key)
    
    print("🔍 Checking available Gemini models for your account...")
    print("-" * 50)
    
    try:
        # List all models
        for m in genai.list_models():
            # We only care about models that can generate content (Chat)
            if 'generateContent' in m.supported_generation_methods:
                print(f"✅ Available: {m.name}")
                
    except Exception as e:
        print(f"❌ Error connecting to Google: {e}")