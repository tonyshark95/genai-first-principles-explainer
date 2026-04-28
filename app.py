import streamlit as st
from ai_service import FirstPrinciplesAI

st.set_page_config(page_title="First-Principles AI", page_icon="🧩", layout="centered")

@st.cache_resource
def get_ai_service():
    return FirstPrinciplesAI()

ai_service = get_ai_service()

if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.title("⚙️ System Architecture")
    st.markdown("""
    **Core Engine:** Google Gemini 2.5 Flash  
    **Frontend:** Streamlit   
    **Architecture:** Modular Service Pattern  
    """)
    
    st.divider()
    st.subheader("🎛️ Engine Tuning")
    temp_setting = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.2, step=0.1)
    st.caption("Lower temperatures enforce deterministic logic. Higher values increase variance.")
    
    st.divider()
    st.subheader("🧠 Explanation Level")
    complexity_setting = st.selectbox(
        "Target Audience", 
        ["Standard First-Principles", "Explain Like I'm 5", "University Level"]
    )

st.title("🧩 First-Principles Deconstructor")
st.markdown("Utilizes an LLM to abstract complex concepts into their fundamental structural logic.")
st.divider()

user_topic = st.text_input("Enter a concept to deconstruct (e.g., Quantum Computing, Inflation):")

if st.button("Analyze Concept", type="primary"):
    if user_topic.strip() == "":
        st.warning("Please enter a valid topic.")
    else:
        with st.spinner("Abstracting concept to fundamental truths..."):
            result = ai_service.deconstruct_topic(user_topic, temp_setting, complexity_setting)
            
            message_placeholder = st.empty()
            full_text = ""
            
            for chunk in result:
                full_text += chunk.text
                message_placeholder.markdown(full_text + "▌")
            
            message_placeholder.markdown(full_text)
            
            st.session_state.history.append({"topic": user_topic, "text": full_text})
            
            st.divider()
            
            st.download_button(
                label="💾 Download Output",
                data=full_text,
                file_name=f"{user_topic.replace(' ', '_')}_notes.txt",
                mime="text/plain"
            )

if st.session_state.history:
    st.divider()
    st.subheader("📚 Session History")
    for i, past_search in enumerate(reversed(st.session_state.history)):
        with st.expander(f"Previous Analysis: {past_search['topic']}"):
            st.markdown(past_search['text'])