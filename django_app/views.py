from http.client import HTTPException
from django.core.cache import caches
from django.shortcuts import render, redirect
from django.urls import reverse

from . import models
from .models import Task

from parsers.weather_parser import get_temp
from parsers.currency_parser import get_currency


def index(request):
    try:
        temperature = get_temp(city='astana')
        tasks = Task.objects.all()

        return render(request, 'index.html', {'temperature': temperature, 'tasks': tasks})

    except Exception as e:
        raise HTTPException(f'{e}')


def request_currency(request):
    try:
        ram_cache = caches['default']
        cached_currency = ram_cache.get('currency')

        if cached_currency is None:
            currency = get_currency()
            ram_cache.set('currency', currency, 60)
            cached_currency = currency

        return render(request, 'currencies.html', {'currency': cached_currency})

    except Exception as e:
        raise HTTPException(f'{e}')


def create_task(request):
    title = str(request.POST['title'])
    description = str(request.POST['description'])
    task = models.Task.objects.create(title=title, description=description)
    task.save()
    return redirect(reverse("index"))


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.title = str(request.POST['edit_title'])
    task.description = str(request.POST['edit_description'])
    if 'edit_completed' in request.POST:
        task.completed = True
    else:
        task.completed = False
    task.save()
    return redirect(reverse("index"))


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect(reverse("index"))
