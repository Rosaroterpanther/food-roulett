from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import random

# Create your views here.
def index(request):
    template = loader.get_template('start/start.html')

    food_id = random.randint(1, 1000)
    context = {
        'random_food_id': food_id
    }
    return HttpResponse(template.render(context, request))

def detail(request, food_id):
    response = "Hello, you search for " + str(food_id) + "."
    return HttpResponse(response)

def add(request):
    return HttpResponse("Nice you wanna add a new food.")
