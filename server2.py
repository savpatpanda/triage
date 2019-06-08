import Triage2
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY']= 'mysecret'
socketio = SocketIO(app)

@app.route('/post', methods = ['POST'])
def postJsonHandler():
    data = request.get_json()
    input_data = [data['1'],
                  data['2'],
                  data['3'],
                  data['4'],
                  data['5'],
                  data['6'],
                  data['7'],
                  data['8'],
                  data['9'],
                  data['10'],
                  data['11'],
                  data['12'],
                  data['13'],
                  data['14'],
                  data['15'],
                  data['16'],
                  data['17'],
                  data['18'],
                  data['19'],
                  data['20'],
                  data['21'],
                  data['22'],
                  data['23'],
                  data['24'],
                  data['25'],
                  data['26'],
                  data['27']]
    predicted_value = Triage2.predict(input_data,2)
    input_data.append(predicted_value)
    send(jsonify(input_data), broadcast=True)

@socketio.on('connection')
def sendValue(msg):
    initial_values = [[45, 'M', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 82, 97, 150, 80, 0, 0, 0, 'AB', 85],
    [15, 'M', 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 30, 75, 100, 60, 0, 0, 0, 'A', 10],
    [17, 'F', 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 60, 80, 70, 30, 0, 0, 0, 'O', 0],
    [30, 'F', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 80, 97, 120, 79, 1, 1, 0, 'AB', 30]]
    send(jsonify(initial_values),broadcast=True)

if __name__ == "__main__":
    app.run(debug=True, port=5000)