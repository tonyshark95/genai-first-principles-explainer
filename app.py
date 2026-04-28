import streamlit as st
from ai_service import FirstPrinciplesAI

# 1. Page Configuration
st.set_page_config(page_title="First-Principles AI", page_icon="🧩", layout="centered")
# --- Sidebar Context ---
with st.sidebar:
    st.title("⚙️ System Architecture")
    # --- Sidebar Context ---
with st.sidebar:
    st.title("⚙️ System Architecture")
    st.markdown("""
    **Core Engine:** Google Gemini 2.5 Flash
    **Frontend:** Streamlit 
    **Architecture:** Modular Service Pattern
    """)
    
    # --- ADD THIS NEW SECTION ---
    st.divider()
    st.subheader("🎛️ Engine Tuning")
    # This creates a slider from 0.0 to 1.0, defaulting to 0.2
    temp_setting = st.slider("Temperature (Logic vs. Creativity)", min_value=0.0, max_value=1.0, value=0.2, step=0.1)
    st.caption("A lower temperature (0.0 - 0.3) forces strict, deterministic logic. Higher values allow the model to take creative liberties.")
    # ----------------------------
    # Add this below your temperature slider
    st.divider()
    st.subheader("🧠 Explanation Level")
    complexity_setting = st.selectbox(
        "Target Audience", 
        ["Standard First-Principles", "Explain Like I'm 5", "University Level"]
    )
    st.markdown("""
    **Core Engine:** Google Gemini 2.5 Flash
    **Frontend:** Streamlit 
    **Architecture:** Modular Service Pattern
    
    **How it works:**
    This system bypasses standard conversational AI guardrails by enforcing a strict prompt architecture, forcing the LLM to strip away analogies and return only foundational, objective truths.
    """)
    st.divider()
    st.caption("Developed for First-Principles Analysis.")

# 2. Initialize the AI Service
# We use st.cache_resource so it only initializes the model once, saving memory
@st.cache_resource
def get_ai_service():
    return FirstPrinciplesAI()

ai_service = get_ai_service()

# --- Initialize Session State (Memory) ---
if "history" not in st.session_state:
    st.session_state.history = []

# 3. Header Section
st.title("🧩 First-Principles Deconstructor")
st.markdown("""
This application utilizes a Generative AI Large Language Model (LLM) to break down complex 
concepts into their fundamental truths, avoiding analogies and focusing on structural logic.
""")
st.divider()

# 4. User Input Area
user_topic = st.text_input("Enter a concept to deconstruct (e.g., Quantum Computing, Inflation, Neural Networks):")

# 5. Execution & Output
if st.button("Analyze Concept", type="primary"):
    if user_topic.strip() == "":
        st.warning("Please enter a valid topic.")
    else:
        with st.spinner("Abstracting concept to fundamental truths..."):
            # Pass all THREE variables to the backend
            result = ai_service.deconstruct_topic(user_topic, temp_setting, complexity_setting)
            
            message_placeholder = st.empty()
            full_text = ""
            
            for chunk in result:
                full_text += chunk.text
                message_placeholder.markdown(full_text + "▌")
            
            message_placeholder.markdown(full_text)
            
            # --- Save to Memory ---
            st.session_state.history.append({"topic": user_topic, "text": full_text})
            
            st.divider()
            
            st.download_button(
                label="💾 Download these First-Principles",
                data=full_text,
                file_name=f"{user_topic.replace(' ', '_')}_notes.txt",
                mime="text/plain"
            )

# 6. Display History
if st.session_state.history:
    st.divider()
    st.subheader("📚 Session History")
    for i, past_search in enumerate(reversed(st.session_state.history)):
        with st.expander(f"Previous Analysis: {past_search['topic']}"):
            st.markdown(past_search['text'])