import streamlit as st
import requests
import json
import base64

# ==========================================
# ☁️ AWS CONFIGURATION
# ==========================================
# PASTE YOUR LAMBDA FUNCTION URL INSIDE THE QUOTES BELOW:
AWS_LAMBDA_URL = "https://3vkrvsogjl4vrgxeotb4i7ammi0jgyon.lambda-url.eu-north-1.on.aws/" 
# Example: "https://abcdefg.lambda-url.us-east-1.on.aws/"

# ==========================================
# 1. Page Config
# ==========================================
st.set_page_config(page_title="BharatFlow.ai", layout="wide")

st.title("🇮🇳 India's Media AI Platform")
st.markdown("### The Unified AI Content Supply Chain (Cloud Mode)")

# ==========================================
# 2. Sidebar for Navigation
# ==========================================
option = st.sidebar.selectbox("Select Module", ["1. The Guardian (Safety)", "2. The Alchemist (Localize)", "3. Player (Delivery)"])

# Helper function to call AWS Lambda
def call_aws_brain(payload):
    try:
        with st.spinner("Connecting to AWS Cloud..."):
            response = requests.post(
                AWS_LAMBDA_URL,
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            if response.status_code == 200:
                return response.json()
            else:
                st.error(f"⚠️ AWS Error {response.status_code}: {response.text}")
                return None
    except Exception as e:
        st.error(f"❌ Connection Failed: {e}")
        return None

# ==========================================
# 3. Module 1: The Guardian
# ==========================================
if option == "1. The Guardian (Safety)":
    st.header("🛡️ Compliance & Safety Audit")
    st.markdown("Analyze scripts or **YouTube videos** for policy violations.")
    
    user_script = st.text_area("Enter text or paste a YouTube URL:", height=150)
    
    if st.button("Analyze for Safety"):
        if user_script:
            # Payload for Lambda
            payload = {
                "task": "guardian",
                "prompt": user_script
            }
            
            result = call_aws_brain(payload)
            
            if result:
                st.subheader("📊 Audit Report")
                
                # Show extracted text (if video)
                if "extracted_text" in result:
                    with st.expander("View Scraped Content"):
                        st.write(result["extracted_text"])
                
                # Show AI Analysis
                report = result.get("guardian_report", "No report generated.")
                st.info(report)
                
        else:
            st.warning("Please enter some text or a URL first.")

# ==========================================
# 4. Module 2: The Alchemist
# ==========================================
elif option == "2. The Alchemist (Localize)":
    st.header("🧪 Hyper-Localization Engine")
    st.markdown("Translate content and generate **Native Audio**.")
    
    input_text = st.text_area("Enter English Content:", height=150)
    target_lang = st.selectbox("Select Target Audience:", ["Hindi", "Tamil", "Bengali", "Spanish", "French"])
    
    if st.button("Localize & Generate Audio"):
        if input_text:
            # Payload for Lambda
            payload = {
                "task": "alchemist",
                "prompt": input_text,
                "target_lang": target_lang
            }
            
            result = call_aws_brain(payload)
            
            if result:
                st.success("Transformation Complete!")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader(f"📝 Script ({target_lang})")
                    translated_text = result.get("translated_text", "Error in translation")
                    st.write(translated_text)
                
                with col2:
                    st.subheader("🎧 Audio Track")
                    audio_b64 = result.get("audio_base64")
                    
                    if audio_b64:
                        # Render Audio Player
                        audio_html = f"""
                            <audio controls autoplay>
                            <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
                            Your browser does not support the audio element.
                            </audio>
                        """
                        st.markdown(audio_html, unsafe_allow_html=True)
                    else:
                        st.warning("Audio could not be generated.")
                    
        else:
            st.warning("Please enter text to localize.")