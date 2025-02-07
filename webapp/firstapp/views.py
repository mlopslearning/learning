from django.shortcuts import render
import yaml,json,os,joblib

def index(request):
    return render(request,'index.html')

def result(request):
    cls=joblib.load("/home/rishabh/Prog/aiml/models/models.joblib/model.joblib")
    list=[]
    list.append(int(request.GET['age']))
    list.append(int(request.GET['sex']))
    list.append(float(request.GET['bmi']))
    list.append(int(request.GET['children']))
    list.append(int(request.GET['region']))
    list.append(int(request.GET['smoker']))

    answer=cls.predict([list])
    
    return render(request,'index.html',{'answer':answer[0]})