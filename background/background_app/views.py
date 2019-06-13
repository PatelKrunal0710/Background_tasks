from django.shortcuts import render,HttpResponse
from background_task import background

def background_view(request):
    hello(repeat=5)
    return HttpResponse("Hello wordl !")


@background(schedule=2)
def hello():
    print("Hello buddy")
