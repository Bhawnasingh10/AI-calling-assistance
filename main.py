import streamlit as st
from voice_handler import listen_and_transcribe, speak_response
from agent import get_agent_response
from conversation import summarize_conversation

st.set_page_config(page_title="AI Call Assistant", layout="centered")

st.title("🎙️ Smart AI Call Assistant (Ollama LLM)")
st.write("Speak into your mic. The assistant will respond and summarize your call.")

if st.button("Start Conversation"):
    transcript = listen_and_transcribe()
    st.subheader("You Said:")
    st.write(transcript)

    response = get_agent_response(transcript)
    st.subheader("AI Says:")
    st.write(response)
    speak_response(response)

    summary = summarize_conversation(f"User: {transcript}\nAI: {response}")
    st.subheader("📝 Summary of Conversation")
    st.write(summary)
