from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main(request):
    n=True
    if n==True:
        return HttpResponse("""Hello my name is Kian Peyrovan.\n kian""")
    
    