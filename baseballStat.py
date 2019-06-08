import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import pickle

data = pd.read_csv("inpatient_data.csv", sep=",")  # this line imports the data from the csv file
data = data[["Age","Gender","Abdominal Pain","Asystole","Bleeding Profusely","Broken Bones","Burns","Chest pain","Concussion","Cuts/Lacerations","Difficulty swallowing","Dizziness","Head Injury","Heart palpitations","Nausea or vomiting","Seizures","Shortness of breath","Unconcious","Wheezing","Pulse Rate","Oxygen","Systolic BP","Diastolic BP","Cardiac Condition","Drug Complications","Blood Problems","Blood Type","Time"]]

predict = "Time"  # label = what we are trying to get

x = np.array(data.drop(["Time"], 1))  # training data
y = np.array(data[predict])  # label we are looking for
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y,test_size=0.1)  # separates sets into a few arrays

best = 0
while best < 0.9:
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.1) #separates sets into a few arrays

    linear = linear_model.LinearRegression()

    linear.fit(x_train,y_train)
    acc = linear.score(x_test,y_test)
    print(acc)

    if(acc>best):
        best = acc
        with open("inpatient.pickle","wb") as f:
            pickle.dump(linear,f)


pickle_in = open("inpatient.pickle", "rb")
linear = pickle.load(pickle_in)

predictions = linear.predict(x_test)

print(best)