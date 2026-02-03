import streamlit as st
from core.guardian import analyze_compliance

# 1. Page Config.....
st.set_page_config(page_title="BharatFlow.ai", layout="wide")

st.title("🇮🇳 India's Media AI Platform")
st.markdown("### The Unified AI Content Supply Chain")

# 2. Sidebar for Navigation
option = st.sidebar.selectbox("Select Module", ["1. The Guardian (Safety)", "2. The Alchemist (Localize)", "3. Player (Delivery)"])

# 3. Module 1: The Guardian
if option == "1. The Guardian (Safety)":
    st.header("🛡️ Compliance & Safety Audit")
    
    # Text Input Area....
    user_script = st.text_area("Enter your script or content here:", height=200)
    
    if st.button("Analyze for Safety"):
        if user_script:
            with st.spinner("Auditing content against policy database..."):
                # Call our function from core/guardian.py
                result = analyze_compliance(user_script)
                
            # Display Result
            if "SAFE" in result:
                st.success("✅ Content is Approved!")
            else:
                st.error("⚠️ Compliance Issues Detected")
                st.markdown(result)
        else:
            st.warning("Please enter some text first :|")

            
# Function 2 alchemist 

elif option == "2. The Alchemist (Localize)":
    st.header("🧪 Hyper-Localization Engine")
    
    input_text = st.text_area("Enter English Content:", height=150)
    target_lang = st.selectbox("Select Target Audience:", ["Hindi", "Tamil", "Bengali", "Telugu", "Kannada"])
    
    if st.button("Localize & Generate Audio"):
        if input_text:
            from core.alchemist import localize_content
            
            with st.spinner(f"Adapting content for {target_lang} audience..."):
                # Call the function
                translated_text, audio_path = localize_content(input_text, target_lang)
            
            # Show Results
            st.subheader(f"📝 Localized Script ({target_lang})")
            st.write(translated_text)
            
            st.subheader("🎧 Native Audio Track")
            st.audio(audio_path)
            
            st.success("Transformation Complete!")
        else:
            st.warning("Please enter text to localize.")