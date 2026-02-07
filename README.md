# 🇮🇳 India's Media Ai (Bharatflow.ai): The Unified Content Supply Chain

![Topic](https://img.shields.io/badge/Focus-Media_%26_Localization-orange)

> **One Input. Infinite Native Experiences.**
>
> *An end-to-end AI pipeline that audits content for safety, localizes it for India's diversity, and adapts it for real-time user engagement.*

---

## 🚩 The Problem
Media creation today is **fragmented, risky, and linear**.
1.  **Risk:** Generative AI creates content faster than humans can verify it for brand safety or legal compliance.
2.  **Language Barrier:** Dubbing is not enough. Content lacks "cultural context" for Tier-2 and Tier-3 Indian audiences.
3.  **Static Delivery:** Users are bored. Video players don't adapt to attention spans or confusion levels.

## 💡 The Solution: A 3-Stage Pipeline
BharatFlow.ai combines **Creation, Management, and Distribution** into a single seamless workflow.

### 1. 🛡️ Stage 1: The Guardian (Compliance & Safety)
* **Automated Auditing:** Scans scripts/video transcripts against a vector database of "Company Policies" and "Legal Truths."
* **Brand Voice Check:** Ensures the tone is empathetic and inclusive.
* **Visual Safety:** Flags competitor logos or copyrighted imagery in video frames.

### 2. 🧪 Stage 2: The Alchemist (Hyper-Localization)
* **Cultural Transcreation:** Doesn't just translate text; it swaps context. (e.g., changes "Dollar/Coffee" to "Rupee/Chai").
* **AI Dubbing:** Generates native-sounding audio in Hindi, Tamil, and Bengali using TTS.
* **Visual Adaptation:** (Demo Feature) Uses Generative In-painting to swap background elements to match the local region.

### 3. ⚡ Stage 3: Adaptive Delivery (Personalized Experience)
* **Smart Player:** An interactive video interface.
* **Attention Loop:** If the user pauses frequently or clicks "I'm confused," the AI instantly generates a **text summary** or simplifies the language.
* **Chat-with-Content:** Users can ask questions to the video and get answers in their local language.

---

## 🛠️ Tech Stack

| Component | Technology Used |
| :--- | :--- |
| **Frontend** | Streamlit (Python) / React.js |
| **LLM Core** | Gemini 2.5 Flash / GPT-4o |
| **Orchestration** | LangChain |
| **Vector DB** | ChromaDB (for Policy/Safety storage) |
| **Voice/Audio** | ElevenLabs API / gTTS |
| **Video Processing**| MoviePy, FFmpeg |
| **Vision** | OpenCV / YOLO (Object Detection) |

---

## ⚙️ Architecture

```mermaid
graph TD
    A[User Input: Raw Video/Script] --> B{The Guardian};
    B -- Safety Fail --> C[Auto-Fix Suggestions];
    B -- Safety Pass --> D{The Alchemist};
    D --> E[Generate Localized Audio];
    D --> F[Contextual Text Rewrite];
    E & F --> G[Final Localized Asset];
    G --> H[Adaptive Player];
    H --> I[User Interaction Loop];
