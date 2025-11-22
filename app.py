from flask import Flask, render_template, redirect, url_for, request, session, jsonify, flash
from datetime import date, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

from database import db, init_db
from models import User, Habit, HabitLog

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///habit_tracker.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'change-this-secret-key'

    init_db(app)

    @app.route('/')
    def index():
        if 'user_id' in session:
            return redirect(url_for('dashboard'))
        return render_template('index.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')

            if not username or not email or not password:
                flash('All fields are required.', 'danger')
                return redirect(url_for('register'))

            if User.query.filter((User.username == username) | (User.email == email)).first():
                flash('Username or email already exists.', 'danger')
                return redirect(url_for('register'))

            user = User(
                username=username,
                email=email,
                password_hash=generate_password_hash(password)
            )
            db.session.add(user)
            db.session.commit()
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))

        return render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter_by(username=username).first()
            if not user or not check_password_hash(user.password_hash, password):
                flash('Invalid username or password.', 'danger')
                return redirect(url_for('login'))

            session['user_id'] = user.id
            session['username'] = user.username
            flash('Logged in successfully.', 'success')
            return redirect(url_for('dashboard'))

        return render_template('login.html')

    @app.route('/logout')
    def logout():
        session.clear()
        flash('Logged out.', 'info')
        return redirect(url_for('index'))

    @app.route('/dashboard')
    def dashboard():
        if 'user_id' not in session:
            return redirect(url_for('login'))

        user_id = session['user_id']
        habits = Habit.query.filter_by(user_id=user_id).all()

        # Calculate basic stats
        today = date.today()
        last_7_days = [today - timedelta(days=i) for i in range(6, -1, -1)]

        completion_data = []
        for d in last_7_days:
            count = HabitLog.query.filter_by(user_id=user_id, date=d).count()
            completion_data.append({
                'date': d.strftime('%Y-%m-%d'),
                'completed': count
            })

        return render_template('dashboard.html', habits=habits, completion_data=completion_data)

    @app.route('/habits', methods=['GET'])
    def get_habits():
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized'}), 401

        user_id = session['user_id']
        habits = Habit.query.filter_by(user_id=user_id).all()

        data = []
        for h in habits:
            data.append({
                'id': h.id,
                'name': h.name,
                'category': h.category,
                'streak': h.streak,
                'created_at': h.created_at.isoformat()
            })

        return jsonify(data)

    @app.route('/habits', methods=['POST'])
    def create_habit():
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized'}), 401

        payload = request.get_json()
        name = payload.get('name')
        category = payload.get('category', 'General')

        if not name:
            return jsonify({'error': 'Name is required'}), 400

        habit = Habit(
            user_id=session['user_id'],
            name=name,
            category=category
        )
        db.session.add(habit)
        db.session.commit()

        return jsonify({'message': 'Habit created', 'id': habit.id}), 201

    @app.route('/habits/<int:habit_id>/complete', methods=['POST'])
    def complete_habit(habit_id):
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized'}), 401

        user_id = session['user_id']
        habit = Habit.query.filter_by(id=habit_id, user_id=user_id).first()
        if not habit:
            return jsonify({'error': 'Habit not found'}), 404

        today = date.today()

        # Check if already logged today
        existing_log = HabitLog.query.filter_by(
            user_id=user_id,
            habit_id=habit.id,
            date=today
        ).first()

        if existing_log:
            return jsonify({'message': 'Already completed today', 'streak': habit.streak})

        # Update streak logic
        if habit.last_completed == today - timedelta(days=1):
            habit.streak += 1
        elif habit.last_completed == today:
            pass
        else:
            habit.streak = 1  # reset and start again

        habit.last_completed = today
        log = HabitLog(user_id=user_id, habit_id=habit.id, date=today)
        db.session.add(log)
        db.session.commit()

        return jsonify({'message': 'Habit completed', 'streak': habit.streak})

    @app.route('/habits/<int:habit_id>/history', methods=['GET'])
    def habit_history(habit_id):
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized'}), 401

        user_id = session['user_id']
        logs = HabitLog.query.filter_by(user_id=user_id, habit_id=habit_id).order_by(HabitLog.date.asc()).all()

        data = [{
            'date': l.date.strftime('%Y-%m-%d')
        } for l in logs]

        return jsonify(data)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
