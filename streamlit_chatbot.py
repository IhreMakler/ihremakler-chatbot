"""
IhreMakler Chatbot App mit ChatGPT Integration
Design basierend auf IhreMakler.online CI
"""

import streamlit as st
import os
from pathlib import Path
from openai import OpenAI

# Seite konfigurieren
st.set_page_config(
    page_title="IhreMakler Chatbot", 
    page_icon="💬", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS für IhreMakler CI
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Main Container */
    .main {
        background-color: #f5f5f5;
    }
    
    /* HEADER STYLING */
    .header-wrapper {
        background-color: #f9f9f9;
        padding: 1rem 0;
        border-bottom: 2px solid #062E52;
    }
    
    .logo-image {
        height: 120px;
        width: auto;
        object-fit: contain;
    }
    
    /* CHAT STYLING */
    .chat-container {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 1.5rem;
        height: 500px;
        overflow-y: auto;
        margin-bottom: 1rem;
        border: 1px solid #e0e0e0;
    }
    
    .chat-message {
        margin-bottom: 1rem;
        padding: 1rem;
        border-radius: 8px;
        font-family: Arial, Verdana, sans-serif;
    }
    
    .chat-message.user {
        background-color: #3B8EA0;
        color: white;
        margin-left: 10%;
        border-radius: 18px 18px 4px 18px;
    }
    
    .chat-message.assistant {
        background-color: #f0f0f0;
        color: #062E52;
        margin-right: 10%;
        border-radius: 18px 18px 18px 4px;
    }
    
    .chat-input-area {
        display: flex;
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .chat-input {
        flex: 1;
        padding: 0.8rem;
        border: 1px solid #3B8EA0;
        border-radius: 4px;
        font-family: Arial, Verdana, sans-serif;
    }
    
    .chat-button {
        background-color: #3B8EA0;
        color: white;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 4px;
        cursor: pointer;
        font-weight: 600;
        font-family: Arial, Verdana, sans-serif;
    }
    
    .chat-button:hover {
        background-color: #2d6b78;
    }
    
    /* MAIN HEADER */
    .main-header {
        background-color: #062E52;
        padding: 3rem 2rem;
        border-radius: 0;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        font-family: Arial, Verdana, sans-serif;
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5em;
        font-weight: 700;
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.1em;
        opacity: 0.9;
    }
    
    /* FOOTER STYLING */
    .footer-container {
        background-color: #f9f9f9;
        border-top: 1px solid #e0e0e0;
        padding: 2rem;
        margin-top: 3rem;
        font-family: Arial, Verdana, sans-serif;
    }
    
    .footer-content {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 2rem;
        margin-bottom: 1.5rem;
    }
    
    .footer-section h4 {
        color: #062E52;
        margin-bottom: 1rem;
        font-size: 1rem;
        font-weight: 700;
        text-align: left;
    }
    
    .footer-section ul {
        list-style: none;
        padding: 0;
        text-align: left;
    }
    
    .footer-section li {
        margin-bottom: 0.5rem;
    }
    
    .footer-section a {
        color: #062E52;
        text-decoration: none;
        font-size: 0.9rem;
        transition: color 0.3s;
    }
    
    .footer-section a:hover {
        color: #3B8EA0;
        font-weight: bold;
    }
    
    .footer-bottom {
        border-top: 1px solid #d0d0d0;
        padding-top: 1.5rem;
        text-align: center;
        color: #666;
        font-size: 0.85rem;
    }
    
    .footer-logo {
        color: #062E52;
        font-weight: 700;
    }
    
    .footer-tagline {
        color: #062E52;
        font-size: 0.85rem;
        font-style: normal;
    }
</style>
""", unsafe_allow_html=True)

# HEADER mit Logo
st.image("https://raw.githubusercontent.com/IhreMakler/altersabfrage-app/main/Logo1.png", width=400)
st.divider()

# Initialize Session State
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

# MAIN HEADER
st.markdown("""
<div class="main-header">
    <h1>IhreMakler Chatbot</h1>
    <p>Stellen Sie Ihre Fragen - Wir helfen Ihnen weiter</p>
</div>
""", unsafe_allow_html=True)

# Chatverlauf direkt unter dem Header
for message in st.session_state.chat_messages:
    if message["role"] == "user":
        st.markdown(f'<div class="chat-message user">{message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-message assistant">{message["content"]}</div>', unsafe_allow_html=True)

# Eingabefeld + Button mit Enter-Support
with st.form("chat_form", clear_on_submit=True):
    col1, col2 = st.columns([9,1])

    with col1:
        user_input = st.text_input(
            "",
            placeholder="Stellen Sie eine Frage...",
            label_visibility="collapsed"
        )

    with col2:
        send_button = st.form_submit_button("Senden", use_container_width=True)

st.markdown("""
<style>

div[data-testid="stFormSubmitButton"] > button {
    background-color: #3B8EA0 !important;
    color: white !important;
    border: none !important;
    border-radius: 4px !important;
    font-weight: 600 !important;
    font-family: Arial, Verdana, sans-serif !important;
    font-size: 1rem !important;
    height: 48px !important;
    padding: 0 2rem !important;
}

div[data-testid="stFormSubmitButton"] > button:hover {
    background-color: #2d6b78 !important;
}


.stTextInput > div > input {
    height: 48px;
    font-size: 1rem;
    padding: 0.8rem;
    border: 1px solid #3B8EA0;
    border-radius: 4px;
    font-family: Arial, Verdana, sans-serif;
    width: 100%;
    display: inline-block;
}
.stButton > button {
    background-color: #3B8EA0;
    color: white;
    border: none;
    border-radius: 4px;
    font-weight: 600;
    font-family: Arial, Verdana, sans-serif;
    font-size: 1rem;
    height: 48px;
    margin-top: 0;
    margin-bottom: 0;
    margin-left: 0.5rem;
    display: inline-block;
    vertical-align: middle;
    padding: 0 2rem;
}
</style>
""", unsafe_allow_html=True)

if send_button and user_input:
    st.session_state.chat_messages.append({"role": "user", "content": user_input})
    st.session_state["chat_input"] = ""
    try:
        api_key = st.secrets.get("OPENAI_API_KEY")
        if not api_key:
            st.error("OpenAI API Key nicht konfiguriert! Bitte in Streamlit Secrets hinzufügen.")
        else:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.chat_messages,
                temperature=0.7,
            )
            assistant_message = response.choices[0].message.content
            st.session_state.chat_messages.append({"role": "assistant", "content": assistant_message})
            st.rerun()
    except Exception as e:
        st.error(f"Fehler beim Abrufen der Antwort: {str(e)}")

# Footer-Überschriften linksbündig
st.markdown("""
<style>
            
.footer-section h4 {
    color: #062E52;
    margin-bottom: 1rem;
    font-size: 1rem;
    font-weight: 700;
    text-align: left;
    margin-left: 0;
}
.footer-section ul {
    text-align: left;
    margin-left: 0;
}
</style>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<style>
    .reportview-container .main footer {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer-container">
    <div class="footer-content">
        <div class="footer-section">
            <h4>Unternehmen</h4>
            <ul>
                <li><a href="https://www.ihremakler.online/team/">Unser Team</a></li>
                <li><a href="https://www.ihremakler.online/">Startseite</a></li>
                <li><a href="https://www.ihremakler.online/immobilienbewertung/">Immobilienbewertung</a></li>
            </ul>
        </div>
        <div class="footer-section">
            <h4>Services</h4>
            <ul>
                <li><a href="https://www.ihremakler.online/immobilie-verkaufen/">Immobilie verkaufen</a></li>
                <li><a href="https://www.ihremakler.online/immobilie-kaufen/">Immobilie kaufen</a></li>
                <li><a href="https://www.ihremakler.online/finanzierungsrechner/">Finanzierungsrechner</a></li>
            </ul>
        </div>
        <div class="footer-section">
            <h4>Rechtliches</h4>
            <ul>
                <li><a href="https://www.ihremakler.online/impressum/">Impressum</a></li>
                <li><a href="https://www.ihremakler.online/datenschutz/">Datenschutz</a></li>
                <li><a href="https://www.ihremakler.online/agb/">AGB</a></li>
                <li><a href="https://www.ihremakler.online/widerrufsbelehrung/">Widerrufsbelehrung</a></li>
            </ul>
        </div>
        <div class="footer-section">
            <h4>Zugang</h4>
            <ul>
                <li><a href="https://www.ihremakler.online/barrierefreiheit/">Barrierefreiheit</a></li>
                <li><a href="https://www.ihremakler.online/#kontakt">Kontakt</a></li>
            </ul>
        </div>
    </div>
    <div class="footer-bottom">
        <p style="margin: 0.5rem 0;">
            <span class="footer-logo">© 2026 Ihre Makler GmbH</span><br>
            <span class="footer-tagline">Lokal • Schnell • Fair</span>
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
