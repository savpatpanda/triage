import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv("inpatient_data.csv")

le = preprocessing.LabelEncoder()
gender = le.fit_transform(list(data["Gender"]))
type = le.fit_transform((list(data["Blood Type"])))

x = list(zip(data["Age"],gender,data["Abdominal Pain"],data["Asystole"],data["Bleeding Profusely"],data["Broken Bones"],data["Burns"],data["Chest pain"],data["Concussion"],data["Cuts/Lacerations"],data["Difficulty swallowing"],data["Dizziness"],data["Head Injury"],data["Heart palpitations"],data["Nausea or vomiting"],data["Seizures"],data["Shortness of breath"],data["Unconcious"],data["Wheezing"],data["Pulse Rate"],data["Oxygen"],data["Systolic BP"],data["Diastolic BP"],data["Cardiac Condition"],data["Drug Complications"],data["Blood Problems"],type))
y = list(data["Time"])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y,test_size = 0.1)

print(x_test)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(x_train,y_train)
acc = model.score(x_test,y_test)
print(acc)

predicted = model.predict(x_test)

for x in range(len(predicted)):
    print("Predicted: ",predicted[x],"Data: ",x_test[x], "Actual: ",y_test[x])
    n = model.kneighbors([x_test[x]],3,True)
    print("N: ",n)