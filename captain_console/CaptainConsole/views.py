from django.shortcuts import render

# Testing -Not supposed to be here, check index.html also
captainconsole = [
    {'name':'Gameboy','price': 39.99},
    {'name':'Gameboy','price': 49.99},
]

def index(request):
    return render(request,'captainconsole/index.html', context={'captainconsole': captainconsole})
