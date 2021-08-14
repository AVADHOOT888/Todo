from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .import models
from django.urls import reverse

# Create your views here.

def home(request):
    todo_items=models.ToDo.objects.all().order_by('-added_date')
    return render(request, 'base.html',{'todo_items':todo_items})

def add_todo(request):
    
    current_date=timezone.now()
    content=request.POST['content']
    created_obj=models.ToDo.objects.create(added_date=current_date, text=content)
    
    return HttpResponseRedirect("/")

def delete_todo(request,todo_id):
    models.ToDo.objects.get(id=todo_id).delete()

    return HttpResponseRedirect("/")


