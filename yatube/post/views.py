from django.http import HttpResponse
from django.shortcuts import render
from re import template
# Create your views here.
def index(request):
    template = 'post/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {
        'title': text,
    }
    return render(request, template, context) 

def group_post(request, pk):
    template = 'post/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': text,
    }
    return render(request, template, context)