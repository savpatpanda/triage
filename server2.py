import Triage2
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, send
import os
app = Flask(__name__)
app.config['SECRET_KEY']= 'mysecret'
socketio = SocketIO(app)

@app.route('/')
def hello():
    return("Hello world!")

@app.route('/post', methods = ['POST'])
def postJsonHandler():
    data = request.get_json()
    input_data = [data['First Name'],
                  data['Last Name'],
                  data['Age'],
                  data['Gender'],
                  data['Abdominal Pain'],
                  data['Asystole'],
                  data['Bleeding Profusely'],
                  data['Broken Bones'],
                  data['Burns'],
                  data['Chest pain'],
                  data['Concussion'],
                  data['Cuts/Lacerations'],
                  data['Difficulty swallowing'],
                  data['Dizziness'],
                  data['Head Injury'],
                  data['Heart palpitations'],
                  data['Nausea or vomiting'],
                  data['Seizures'],
                  data['Shortness of breath'],
                  data['Unconscious'],
                  data['Wheezing'],
                  data['Pulse Rate'],
                  data['Oxygen'],
                  data['Systolic BP'],
                  data['Diastolic BP'],
                  data['Cardiac Condition'],
                  data['Drug Complications'],
                  data['Blood Problems'],
                  data['Blood Type']]
    predicted_value = Triage2.predict(input_data,2)
    print("The person's value for this patient is: %f" % predicted_value)
    input_data.append(predicted_value)
    resp = jsonify(input_data)
    '''send(jsonify(input_data), broadcast=True)'''
    return resp

@socketio.on('connection')
def sendValue(msg):
    initial_values = [['James','Smith',45, 'M', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 82, 97, 150, 80, 0, 0, 0, 'AB', 85],
    ['James','Jones',15, 'M', 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 30, 75, 100, 60, 0, 0, 0, 'A', 10],
    ['Janet','Yellin',17, 'F', 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 60, 80, 70, 30, 0, 0, 0, 'O', 0],
    ['Aneesha','Atri',30, 'F', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 80, 97, 120, 79, 1, 1, 0, 'AB', 30]]
    send(jsonify(initial_values),broadcast=True)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', '5000'))
    app.run(host= '0.0.0.0', port=port)