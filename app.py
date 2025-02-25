from components.chatbot import get_response
import streamlit as st

st.set_page_config(page_title="Arushi's Assistant", page_icon="🤖")

st.markdown("""
    <h1 style="text-align: center;">🤖 Hi, I am Albert - Arushi's Assistant</h1>
""", unsafe_allow_html=True)

st.markdown("""
    <p style="text-align: center; font-size:18px;">
        You can ask me about Arushi's professional background, experience, and achievements.
    </p>
""", unsafe_allow_html=True)

# Custom CSS for message alignment
st.markdown("""
    <style>
        .user-message {
            text-align: right;
            padding: 10px;
            outline: 1px solid #82b2ff;
            
            border-radius: 10px;
            max-width: 75%;
            margin-left: auto;
            margin-bottom: 10px;
        }
        .bot-message {
            text-align: left;
            padding: 10px;
            outline: 1px solid #990383;
            border-radius: 10px;
            max-width: 75%;
            margin-right: auto;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history with alignment
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message">{message["content"]}</div>', unsafe_allow_html=True)

# User input at the bottom
query = st.chat_input("Ask a question...")

if query:
    # Add user message (right-aligned)
    st.session_state.messages.append({"role": "user", "content": query})
    st.markdown(f'<div class="user-message">{query}</div>', unsafe_allow_html=True)

    with st.spinner("Processing..."):
        response = get_response(query)
    
    # Add bot response (left-aligned)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.markdown(f'<div class="bot-message">{response}</div>', unsafe_allow_html=True)
