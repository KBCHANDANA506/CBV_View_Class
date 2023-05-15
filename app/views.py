from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *


# Create your views here.


# by sunig fbv 
def fbv_string(request):
    return HttpResponse("This is fvb string")

#by using cbv

class Cbv_string(View):
    def get(self,request):
        return HttpResponse("This is cbv string")

#rendering html page by using fbv html

def fbv_html(request):

    return render(request,'fbv_html.html')

class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')
#rendering form by using fbv

def fbv_form(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data inserted successfullyyy.....!')

    return render(request,'fbv_form.html',d)


#handling model form by using cbv

class cbv_form(View):
    def get(self,request):
        TFO=TopicForm()
        d={'TFO':TFO}
        return render(request,'cbv_form.html',d)

    def post(self,request):
        TFD=TopicForm()
        if TFD.is_valid():
            TFD.save()
        return HttpResponse('data inserted successfully....!')











