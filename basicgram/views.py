from django.http.response import HttpResponse
import json

def sort_numbers(request):
    ''' Receive a list of numbers and return the list in order'''
    # import pdb; pdb.set_trace()
    numbers = request.GET['numbers'].split(',')
    numbers = [int(nr) for nr in numbers]
    numbers = sorted(numbers)
    dictionary = {
        'status' : 'OK',
        'numbers': numbers,
        'message': 'Numbers succesfully sorted'
    }
    return HttpResponse(json.dumps(dictionary), content_type='application/json')


def say_hi(request, name, age):
    ''' Say hi to a person and verify his/her age'''
    hi_msg = f'Hi {name} '
    age_msg = 'you are under-age' if age < 18 else 'you are major'
    return HttpResponse(hi_msg + age_msg)