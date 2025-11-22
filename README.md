# 🌿 Daily Habit Tracker (Flask + SQLite + Chart.js)

A clean, minimal **daily habit tracker** built with **Python (Flask)**, **SQLite**, and **HTML/CSS/JavaScript**.  
Users can create habits, mark them as complete each day, and track streaks and weekly completions with charts.

---

## ✨ Features

- User registration and login
- Create habits with name + category
- Daily completion tracking
- Automatic streak calculation
- Weekly completion stats (last 7 days)
- Dashboard with bar chart using Chart.js
- Dark, modern UI

---

## 🧱 Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Database:** SQLite
- **Frontend:** HTML, CSS, Vanilla JavaScript
- **Charts:** Chart.js

---

## 📂 Project Structure

```bash
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

## 🚀 Getting Started (Local Setup)

### 1️⃣ Clone the repo

```bash
git clone https://github.com/<your-username>/habit-tracker.git
cd habit-tracker
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app

```bash
python run.py
```

Then open your browser at:  
`http://127.0.0.1:5000`

---

## 🔐 Default Config

- Uses `SECRET_KEY` in `app.py` – change it before deploying.
- SQLite DB file: `habit_tracker.db` (auto-created).

---

## 🧮 Streak Logic

- If you complete a habit:
  - **Yesterday was last completion** → streak +1  
  - **Already completed today** → no change  
  - **Missed a day** → streak resets to 1  

---

## 🛠 Possible Extensions

- Email reminders for habits
- Calendar view per habit
- Categories filter & search
- Mobile responsive enhancements
- Export data as CSV

---

## 📸 Screenshots
<div align="center">
🔐 Login Page
<img src="https://github.com/user-attachments/assets/b0232156-78bf-46e2-9cf4-5c064537d4f2" width="70%" style="border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);" />
📝 Sign Up Page
<img src="https://github.com/user-attachments/assets/1850e63f-3008-4a11-8912-3cdc7c57261c" width="70%" style="border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);" />
📊 Dashboard
<img src="https://github.com/user-attachments/assets/cf9838dc-7364-4db0-8cf6-623442bad011" width="70%" style="border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);" />
🚪 After Logout
<img src="https://github.com/user-attachments/assets/4996c191-a327-4764-a84d-b4318d45aada" width="70%" style="border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);" /> </div>
---

## 📜 License

MIT – Feel free to use, modify, and learn from it.
