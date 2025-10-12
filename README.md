# 🧠 WEB-DEV-PROJECTS

Welcome to **WEB-DEV-PROJECTS**, a curated collection of **Full-Stack Web Development projects** built using **Python, Django, HTML, CSS, JavaScript, and modern web technologies**.  
Each project demonstrates practical implementations of backend logic, REST APIs, database integrations, and front-end UI/UX designs.

---

## 📁 Repository Structure

```
WEB-DEV-PROJECTS/
│
├── BlogProject/                      # Full-stack Django Blog Application
│   ├── BlogProject/                  # Core Django settings and config files
│   ├── posts/  
│   ├── templates/                    # Shared HTML templates
│   ├── db.sqlite3                    # Local SQLite database
│   ├── manage.py
│   └── requirements.txt
│
├── LegalDoc-AI_P/                    # AI-based Legal Document Assistant
│   ├── app.py                        # Flask/Django app file
│   ├── templates/                    # HTML templates
│   ├── static/                       # CSS, JS, and assets
│   ├── uploads/                      # Uploaded documents
│   ├── instance/legal_assistant.db   # SQLite Database
│   ├── requirements.txt
│   └── .gitignore
│
└── README.md
```

---

## ⚙️ Tech Stack

**Frontend:**
- HTML5, CSS3, JavaScript
- Tailwind CSS / Bootstrap
- Responsive Web Design  

**Backend:**
- Python (3.10+)
- Django Framework
- Flask (for lightweight apps)
- REST APIs

**Database:**
- SQLite (Local Development)
- PostgreSQL / MySQL (Production Ready)

**Tools & Environment:**
- VS Code
- Git & GitHub
- Virtual Environment (venv)
- Django Admin Panel
- Jinja2 / Django Template Engine

---

## 🚀 Features

- 🧩 Modular Project Structure (multiple apps)
- 📚 Full CRUD functionality
- 🔒 User Authentication (Login / Signup)
- 🧠 AI-Powered Legal Assistant (Flask + NLP)
- 🌐 Responsive Frontend UI
- ⚡ Dynamic Routing and API Integration
- 📦 Easy Setup and Deployment Ready

---

## 🛠️ Local Setup Guide

Follow these steps to run the projects locally 👇

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/WEB-DEV-PROJECTS.git                        # for all projects

git clone https://github.com/ShivanshGupta-25/Web-Dev-Projects/tree/main/BlogProject      # for BlogProject

git clone https://github.com/ShivanshGupta-25/Web-Dev-Projects/tree/main/LegalDoc-AI_P   # for LegalDoc-AI_P

# change the directory to the cloned project folder
cd BlogProject

# then navigate to the project folder
cd BlogProject

# or for LegalDoc-AI_P
cd LegalDoc-AI_P
```

### 2️⃣ Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # For Linux/Mac
venv\Scripts\activate           # For Windows
```

### 3️⃣ Install Dependencies
Each project has its own `requirements.txt`.  
Install dependencies accordingly:

**For BlogProject:**
```bash
cd BlogProject
pip install -r requirements.txt
```

**For LegalDoc-AI_P:**
```bash
cd LegalDoc-AI_P
pip install -r requirements.txt
```

### 4️⃣ Run Django Server
```bash
python manage.py migrate
python manage.py runserver
```
Open in browser → [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 5️⃣ Run Flask App (for LegalDoc-AI_P)
```bash
python app.py
```
Open in browser → [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📸 Preview

| Project | Description |
|----------|--------------|
| 📰 **BlogProject** | A Django-based blog platform supporting CRUD posts, admin dashboard, and authentication. |
| ⚖️ **LegalDoc-AI_P** | An AI-powered assistant that analyzes and processes legal documents using NLP techniques. |

---

## 💡 How to Contribute

Contributions are welcome!  

1. **Fork** the repository  
2. **Create a new branch**  
   ```bash
   git checkout -b feature-branch
   ```
3. **Make your changes**
4. **Commit** and **Push**
   ```bash
   git commit -m "Added new feature"
   git push origin feature-branch
   ```
5. **Create a Pull Request**

---

## ❤️ Support the Developer

If you find this project helpful or inspiring:

⭐ **Star this repo**  
🔁 **Share it with others**  

---

## 📬 Contact

👤 **Shivansh Gupta**
📧 **Email:** [Shivansh Gupta](mailto:shivansh.gupta.25@gmail.com)
💼 **LinkedIn:** [LinkedIn](https://www.linkedin.com/in/shivansh-gupta-25/)
---

## 🧾 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- **Django & Flask Documentation**
- **Bootstrap / Tailwind CSS**
- **OpenAI & NLP Libraries**
- **Community Contributors**

---

## 💪 Final Words

> “Code, Create, Contribute — because every project adds a new skill to your story.” 🚀
