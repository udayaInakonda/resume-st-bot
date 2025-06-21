import streamlit as st
import os
import json

# Load password from secrets.json
# with open("secrets.json", "r") as secret_file:
#     secrets = json.load(secret_file)
# APP_PASSWORD = secrets.get("password", "")

# Password protection
def check_password():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if st.session_state["authenticated"]:
        return True

    password = st.text_input("🔐 Enter Access Password:", type="password")
    if password == st.secrets["app_password"]:
        st.session_state["authenticated"] = True
        st.success("✅ Access granted.")
        st.experimental_rerun()
    elif password:
        st.error("❌ Incorrect password.")
    return False



if not check_password():
    st.stop()

# Page config
st.set_page_config(page_title="Udaya - An Aspiring AI Engineer's Bot", page_icon="🤖", layout="centered")

# Header
st.title("🤖 Chat with Udaya - An Aspiring AI Engineer's Bot")
st.markdown("Ask me about my skills, experience, or projects!")

# Chat input (pre-populated from suggestions if clicked)
user_input = st.text_input("You:", value=st.session_state.get('user_input_box', ''), placeholder="e.g. Tell me about your projects")

# Load Q&A from context.txt
def load_context(context_path="context.txt"):
    qa_pairs = {}
    if not os.path.exists(context_path):
        return qa_pairs
    with open(context_path, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                q, a = line.strip().split(":", 1)
                qa_pairs[q.strip().lower()] = a.strip()
    return qa_pairs

context_qa = load_context()

# Save unknown question
def save_feedback_to_file(question, feedback_path="feedback.txt"):
    with open(feedback_path, "a", encoding="utf-8") as f:
        f.write(question.strip() + "\n")
    return True

# Skills rating dictionary
skills_rating = {
        "Python": 3,
        "Machine Learning": 2,
        "Hugging Face Transformers": 3,
        "Generative AI / LangChain / RAG": 3,
        "Angular": 4,
        ".NET Core": 3,
        "MySQL": 4,
        "Git": 5
}

def show_skill_cards():
    st.markdown("### 🧠 My Skill Levels")
    for skill, rating in skills_rating.items():
        stars = "⭐" * rating + "☆" * (5 - rating)
        st.markdown(f"**{skill}**: {stars}")

# Function to get response
def get_bot_response(message):
    msg = message.lower().strip()
    # First try exact match
    if msg in context_qa:
        return context_qa[msg]
    # Then try partial match
    for q, a in context_qa.items():
        if q in msg:
            return a
    return None

# Main logic
if user_input:
    st.markdown(f"**You:** {user_input}")
    response = get_bot_response(user_input)

    if response:
        st.markdown(f"**UdayaBot:** {response}")

        # If user asked about skills, show detailed skill view option
        if "skill" in user_input.lower():
            if st.button("🔍 View Detailed Skill Levels"):
                show_skill_cards()
    else:
        st.markdown(f"**UdayaBot:** Oops! I don’t have an answer for that yet.")
        st.info("Would you like to send this feedback to the dev?")
        if st.button("Yes, send feedback to dev!"):
            if save_feedback_to_file(user_input):
                st.success("Feedback received! Udaya is always learning. 💡")
            else:
                st.error("Something went wrong while saving feedback.")

        # Show fallback suggestions
        st.markdown("### 💡 Try asking about:")
        suggestions = ["Skills", "Projects", "Experience","Notice Period","Strengths"]
        cols = st.columns(len(suggestions))
        for i, q in enumerate(suggestions):
            if cols[i].button(q):
                st.session_state['user_input_box'] = q
                st.rerun()

# Divider
st.markdown("---")

# Resume download
st.subheader("📄 Download My Resume")
with open("UDAYA.I_AI (10).pdf", "rb") as f:
    resume_data = f.read()
st.download_button("Download Resume", resume_data, file_name="UDAYA.I_AI (10).pdf", mime="application/pdf")

# Contact links
st.markdown("---")
st.subheader("📬 Let's Connect!")
st.markdown("🔗 [GitHub](https://github.com/udayaInakonda) | [LinkedIn](https://linkedin.com/in/udaya-i-a919b6191)")
