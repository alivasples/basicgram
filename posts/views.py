from django.shortcuts import render
from datetime import datetime
from django.http.response import HttpResponse

posts = [
    {
        'title': 'Cars',
        'user': {
            'name': 'John Smith',
            'photo': 'https://bootdey.com/img/Content/avatar/avatar7.png'
        },
        'timestamp': datetime.now().strftime('%Y-%m-%d'),
        'content': 'This is my car. Lol!',
        'picture': 'http://commondatastorage.googleapis.com/codeskulptor-demos/riceracer_assets/img/car_2.png'
    },
    {
        'title': 'The Universe',
        'user': {
            'name': 'Carl Sagan',
            'photo': 'https://bootdey.com/img/Content/avatar/avatar1.png'
        },
        'timestamp': datetime.now().strftime('%Y-%m-%d'),
        'content': 'I present a photo of a galaxy',
        'picture': 'http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.s2014.png'
    }
]

def list_posts(request):
    return render(request, 'feed.html', {'posts': posts})