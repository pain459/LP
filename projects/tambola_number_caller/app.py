from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

# Store the called numbers
called_numbers = []

@app.route('/')
def index():
    return render_template('index.html', numbers=range(1, 91), called_numbers=called_numbers)

@app.route('/call-number', methods=['POST'])
def call_number():
    number = int(request.form.get('number'))
    if number not in called_numbers:
        called_numbers.append(number)
    return jsonify(success=True, number=number)

if __name__ == '__main__':
    app.run(debug=True)
