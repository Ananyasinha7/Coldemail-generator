# ✉️ Cold Email Generator – GenAI Tool

**Cold Email Generator** is an end-to-end GenAI application designed to help software and AI services companies craft high-quality cold emails tailored to potential clients. Built with open-source LLMs and vector search, it streamlines outreach with context-aware personalization.

---

## 🧠 Technologies Used

- **LLaMA 3 (Meta AI)** – Open-source large language model for generating high-quality emails.
- **LangChain** – Framework for chaining LLMs, agents, and tools in a modular way.
- **FAISS** – Fast, open-source vector similarity search library (via LangChain Community).
- **Streamlit** – Interactive UI for seamless user experience in the browser.
- **Pandas** – For data manipulation and CSV handling.

---

## 🚀 Features

- **URL-based Content Extraction** – Scrapes and processes client websites to understand their offerings.
- **Context-Aware Job Matching** – Identifies relevant services or job opportunities from web content.
- **Cold Email Generation** – Crafts personalized emails based on services matched to the company profile.
- **Portfolio Link Matching** – Recommends relevant portfolio links based on extracted skills.
- **Vector-Based Memory (FAISS)** – Stores and queries past client data using embeddings.
- **Interactive Web Interface** – User-friendly Streamlit frontend.

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Ananyasinha7/Coldemail-generator.git
cd Coldemail-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the `app/` directory with your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

Or, if deploying to Streamlit Cloud, add your API key in the secrets section.

---

## 🖥️ Usage

```bash
streamlit run app/main.py
```

- Enter a client website URL.
- The app will extract job/service info, match relevant portfolio links, and generate a personalized cold email.

---

## 📁 Project Structure

```
cold-email-generator/
│
├── app/
│   ├── chains.py
│   ├── main.py
│   ├── portfolio.py
│   ├── utils.py
│   └── resource/
│       └── my_portfolio.csv
├── requirements.txt
├── README.md
└── vectorstore/
```

---

## 📝 Notes

- Make sure your `my_portfolio.csv` is correctly formatted and placed in `app/resource/`.
- For deployment on Streamlit Cloud, add your API key in the secrets section.
- If using FAISS, ensure `faiss-cpu` is installed (see requirements).

---

## 📄 License

MIT License

---
