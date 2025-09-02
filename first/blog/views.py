from django.shortcuts import render
from django.http import HttpResponse as http
import django
# Create your views here.
def index(request):
    n=input("what is your name:")
    if "," in n:
        last,first=n.split(",")
        last=last.strip()
        first=first.strip()
        return http(f"Hello, {first.title()} {last.title()}")
    else:
     return http(f"Hello, {n}")
    