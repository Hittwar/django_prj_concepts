"""Platzigram views"""
#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
import json

def hello_world(request):
    """ return a greeting"""
    return HttpResponse('Oh, Hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))

def sort_integers(request):
    """return a JSON"""
    numbers = [int(i) for i in (request.GET['numbers'].split(','))]
    sorted_ints = sorted(numbers)
    data = {
        'status':'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succesfully'
    }

    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {} welcome to join'.format(name)
    
    return HttpResponse(message)
