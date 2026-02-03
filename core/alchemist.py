import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from gtts import gTTS

# Initialize the Model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

def localize_content(text_content, target_language):
    """
    1. Culturally adapts and translates text.
    2. Generates an audio file for the translated text.
    """
    
    # --- Step A: AI Adaptation ---
    template = """
    You are a professional localization expert for the Indian market.
    Your task:
    1. Translate the following script into {language}.
    2. ADAPT cultural references. (Example: If the text says 'Grab a coffee', change it to something culturally relevant like 'Chai' if appropriate for the region).
    3. Keep the tone consistent.

    Original Script: "{text}"
    
    Return ONLY the final translated text. No explanations.
    """
    
    prompt = PromptTemplate(template=template, input_variables=["language", "text"])
    chain = prompt | llm
    
    # Get the translated text
    translated_text = chain.invoke({"language": target_language, "text": text_content}).content
    
    # --- Step B: Audio Generation (TTS) ---
    # Map languages to gTTS codes
    lang_codes = {
        "Hindi": "hi",
        "Tamil": "ta",
        "Bengali": "bn",
        "Telugu": "te",
        "Kannada": "kn"
    }
    
    # Default to English 'en' if language not found
    code = lang_codes.get(target_language, "en")
    
    # Generate Audio
    tts = gTTS(text=translated_text, lang=code, slow=False)
    
    # Save the file
    filename = f"assets/audio_{code}.mp3"
    
    # Ensure assets folder exists
    os.makedirs("assets", exist_ok=True)
    
    tts.save(filename)
    
    return translated_text, filename