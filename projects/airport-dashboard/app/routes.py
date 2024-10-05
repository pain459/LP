# app/routes.py
from flask import request, jsonify, render_template
from app import app, db
from app.models import Flight

@app.route('/')
def dashboard():
    flights = Flight.query.all()
    return render_template('index.html', flights=flights)

@app.route('/api/flights', methods=['GET'])
def get_flights():
    flights = Flight.query.all()
    return jsonify([{
        'from': flight.from_location,
        'to': flight.to_location,
        'flight_number': flight.flight_number,
        'status': flight.status
    } for flight in flights])

@app.route('/api/flights', methods=['POST'])
def add_flight():
    data = request.json
    new_flight = Flight(
        from_location=data['from'],
        to_location=data['to'],
        flight_number=data['flight_number'],
        status=data['status']
    )
    db.session.add(new_flight)
    db.session.commit()
    return jsonify({'message': 'Flight added successfully'})

@app.route('/api/flights/<int:id>', methods=['PUT'])
def update_flight(id):
    flight = Flight.query.get(id)
    data = request.json
    flight.from_location = data['from']
    flight.to_location = data['to']
    flight.flight_number = data['flight_number']
    flight.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Flight updated successfully'})

@app.route('/api/flights/<int:id>', methods=['DELETE'])
def delete_flight(id):
    flight = Flight.query.get(id)
    db.session.delete(flight)
    db.session.commit()
    return jsonify({'message': 'Flight deleted successfully'})
