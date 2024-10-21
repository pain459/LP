from flask import Flask, render_template, request, redirect, url_for
from models import db, Income, Expense

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    incomes = Income.query.all()
    expenses = Expense.query.all()

    # Calculate total income and total expense
    total_income = db.session.query(db.func.sum(Income.amount)).scalar() or 0
    total_expense = db.session.query(db.func.sum(Expense.amount)).scalar() or 0
    balance = total_income - total_expense

    return render_template('index.html', incomes=incomes, expenses=expenses, balance=balance)

@app.route('/add_income', methods=['POST'])
def add_income():
    amount = request.form['amount']
    category = request.form['category']
    income = Income(amount=amount, category=category)
    db.session.add(income)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    amount = request.form['amount']
    category = request.form['category']
    expense = Expense(amount=amount, category=category)
    db.session.add(expense)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
