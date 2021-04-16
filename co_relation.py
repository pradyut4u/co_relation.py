import plotly.express as pe
import csv
import numpy as np

def getdata(path):
    rollno=[]
    marksinpercentage=[]
    dayspresent=[]
    with open(path)as f:
        reader=csv.DictReader(f)
        for row in reader:
            print(row)
            rollno.append(float(row["Roll No"]))
            marksinpercentage.append(float(row["Marks In Percentage"]))
            dayspresent.append(float(row["Days Present"]))
    return {"x":rollno,"y":marksinpercentage,"z":dayspresent}

def findcorelation(data):
    corelation=np.corrcoef(data["x"],data["y"])
    corelation1=np.corrcoef(data["x"],data["z"])
    corelation2=np.corrcoef(data["y"],data["z"])
    print(corelation[0,1])
    print(corelation1)
    print(corelation2)

def setup():
    path="co_relation.csv"
    data=getdata(path)
    findcorelation(data)

setup()