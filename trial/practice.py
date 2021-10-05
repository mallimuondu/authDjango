from django.contrib.auth import authenticate, login
from django import template

oof = template.Library()
@oof.assignment_tag

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return "yay"
    else:
       return "ohh no shoot"
