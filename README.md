# habit_tracker
Say less J — here’s a **drip-heavy, GitHub-optimized, recruiter-friendly README.md** for your Habit Tracker project.
It’s clean, aesthetic, and screams *“hire me, I build real stuff”*.

Copy-paste this straight into your repo.

---

# 🌿 **Daily Habit Tracker — Full-Stack Flask App**

*A clean & modern productivity app to build habits, track streaks, and stay consistent.*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Flask-Framework-orange?style=for-the-badge&logo=flask" />
  <img src="https://img.shields.io/badge/SQLite-Database-003b57?style=for-the-badge&logo=sqlite" />
  <img src="https://img.shields.io/badge/Chart.js-Visualizations-ff6384?style=for-the-badge&logo=chartdotjs" />
  <img src="https://img.shields.io/badge/Status-Live-success?style=for-the-badge" />
</p>

---

## 🌟 **What this project does**

This app helps users build discipline by tracking daily habits.
It includes:

* 🔥 Streak system (auto-reset on missed days)
* 📊 Weekly analytics with Chart.js
* ➕ Add habits
* ✅ Mark habits as complete
* 👤 Login / Register
* 🌓 Beautiful dark theme
* 📁 SQLite backend
* 🤝 Full CRUD API

Perfect for real-world usage and a killer addition to your GitHub portfolio.

---

## 📸 **Screenshots**

> Add your own screenshots after running the project

| Dashboard     | Weekly Stats  |
| ------------- | ------------- |
| *(add image)* | *(add image)* |

---

## 🚀 **Tech Stack**

### **Frontend**

* HTML5
* CSS3 (dark UI)
* Vanilla JavaScript
* Chart.js

### **Backend**

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* Werkzeug Auth

---

## 🧩 **Features Breakdown**

### ✅ **Habit Management**

* Create habits with category
* Mark as complete
* Track streaks
* Track history

### 📊 **Dashboard Analytics**

* Last 7 days completion chart
* Streak counter
* Visual insights

### 🔐 **Authentication**

* Login
* Register
* Secure password hashing

### 📱 **UI / UX**

* Fully responsive
* Dark minimal theme
* Smooth interactions

---

## 📂 **Project Structure**

```
habit-tracker/
├── app.py
├── database.py
├── models.py
├── run.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── dashboard.js
```

---

## ⚙️ **Installation & Setup**

### **1️⃣ Clone the repo**

```bash
git clone https://github.com/<your-username>/habit-tracker.git
cd habit-tracker
```

### **2️⃣ Create a virtual environment**

```bash
python -m venv venv
```

### **Activate it:**

* Windows

  ```bash
  venv\Scripts\activate
  ```
* Mac/Linux

  ```bash
  source venv/bin/activate
  ```

### **3️⃣ Install dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Run the server**

```bash
python run.py
```

### **5️⃣ Open in browser**

```
http://127.0.0.1:5000
```

---

## 🔥 **Streak Logic Explained**

The vibe is simple:

```
If last completed == yesterday → streak + 1  
If last completed == today → ignore  
Else → streak resets to 1  
```

Keeps users accountable like a real productivity app.

---

## 📦 **Future Upgrades (if you wanna evolve it later)**

* 📅 Calendar view per habit
* 🔔 Email or push reminders
* 🏆 Habit badges / achievements
* 📤 Export stats to CSV
* 🌓 Light mode toggle
* 🧠 Simple ML model to predict habit consistency

---

## ❤️ **Why this project is resume-worthy**

* Full-stack
* Real functionality
* APIs + DB + Auth + UI
* Clean code
* Expandable
* Looks 🔥 in a GitHub portfolio
* Perfect for internships, Jr dev roles, or showcasing Python skill

---

## 📝 **License**

MIT License — free to use, modify, and learn from.

---

## 🙌 **Star the repo if you like it**

It helps your profile + makes the project look active ✨

---


✅ A demo GIF
Just say **“banner”**, **“create description”**, or **“generate screenshots”**.
