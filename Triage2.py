import pandas as pd
import math
import operator
from sklearn import preprocessing
from flask import jsonify

data = pd.read_csv("inpatient_data.csv")

le = preprocessing.LabelEncoder()
gender = le.fit_transform(list(data["Gender"]))
type = le.fit_transform((list(data["Blood Type"])))

x = list(zip(data["First Name"],data["Last Name"],data["Age"],gender,data["Abdominal Pain"],data["Asystole"],data["Bleeding Profusely"],data["Broken Bones"],data["Burns"],data["Chest pain"],data["Concussion"],data["Cuts/Lacerations"],data["Difficulty swallowing"],data["Dizziness"],data["Head Injury"],data["Heart palpitations"],data["Nausea or vomiting"],data["Seizures"],data["Shortness of breath"],data["Unconscious"],data["Wheezing"],data["Pulse Rate"],data["Oxygen"],data["Systolic BP"],data["Diastolic BP"],data["Cardiac Condition"],data["Drug Complications"],data["Blood Problems"],type))
y = list(data["Time"])

def euclideanDistance(instance1, instance2, length):
    squared_distance = 0
    for i in range(2,27):
        squared_distance += (int(instance1[i])-int(instance2[i]))**2
    return math.sqrt(squared_distance)

def getNeighbors(tester, k):
    list_o_neighbors = []
    for i in range(len(x)):
        list_o_neighbors.append((euclideanDistance(tester,x[i],len(tester)),x[i],y[i]))
    list_o_neighbors.sort(key=operator.itemgetter(0))
    neighbors = []
    for i in range(k):
        neighbors.append(list_o_neighbors[i])
    return neighbors

def predict(input,k):
    le.fit_transform(list(data['Gender']))
    le.fit_transform(list(data['Blood Type']))
    neighbors = getNeighbors(input,k)
    sum_of_distances = 0
    for i in range(len(neighbors)):
        print(neighbors[i][0])
        sum_of_distances += neighbors[i][0]
    prediction = 0
    for i in range(len(neighbors)):
        prediction = prediction + (neighbors[i][0]/sum_of_distances)*neighbors[i][2]
    return prediction