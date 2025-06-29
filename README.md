
# 🤖 Udaya's AI Assistant – Portfolio Chatbot

A **Streamlit-based personal chatbot** designed as an interactive portfolio and Q&A bot for **Udaya Lakshmi Neelima Inakonda**, an aspiring AI Engineer and Full Stack Developer. The bot answers questions about Udaya’s background, skills, and experience using a rule-based knowledge base and collects feedback for continuous improvement.

---

## 🚀 Features

### 🔐 Password Protection

- Secured with a password prompt.
- Uses `secrets.json` to store credentials (excluded via `.gitignore`).

### 💬 Smart Chatbot

- Responds to predefined Q&A from `context.txt`.
- If the question is unknown, logs it to `feedback.txt` and prompts the user for input.

### ⭐ Skill Ratings

- Displays a visual star-based rating card of Udaya’s technical skills (Python, ML, Git, etc.).

### 📄 Resume Download

- Provides a button to download the latest resume.

### 🔗 Contact Info

- Includes clickable links to:
  - [GitHub](https://github.com/udayaInakonda)
  - [LinkedIn](https://linkedin.com/in/udayalakshmineelima)

### 💡 Suggestion Bubbles

- Shows helpful question suggestions when the chatbot doesn't know the answer.

### 🌙 Theme Toggle

- Toggle between dark and light themes using a Sun/Moon button with custom CSS styling.

---

## 📁 Project Structure

```
📆 Crop_Recommendation_Chatbot
🗂 app.py                  # Main Streamlit app
🗂 context.txt             # Rule-based Q&A data
🗂 feedback.txt            # Stores unanswered user queries
🗂 resume.pdf     # Resume file
🗂 requirements.txt        # Python dependencies
🗂 secrets.json            # (Excluded from git) Password storage
🗂 .gitignore              # Ignores virtual envs and sensitive files
🗂 README.md               # This file
```

---

## 🧠 How It Works

1. **User logs in** with a password.
2. **Asks a question.**
   - If matched in `context.txt`, the bot responds.
   - If not, a fallback message appears with feedback option and suggestions.
3. **User can:**
   - View skill ratings
   - Download resume
   - Contact via GitHub/LinkedIn
   - Switch themes (light/dark)

---

## 🛠 Technologies Used

- [Python 3.x](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- Custom CSS for theming
- File I/O for simple state and feedback management

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/portfolio-chatbot.git
cd portfolio-chatbot

# (Optional) Create and activate your virtual environment
conda create -n chatbot-env python=3.10
conda activate chatbot-env

# Install required dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

---

## 🧹 Future Enhancements

- Add chatbot memory/context using LangChain or LLMs
- Admin panel for managing feedback and updating context
- Persistent database (e.g., SQLite) for context and feedback
- Voice interface integration

---

## 🙌 Acknowledgements

Developed by [Udaya Lakshmi Neelima Inakonda](https://www.linkedin.com/in/udayalakshmineelima)

---
