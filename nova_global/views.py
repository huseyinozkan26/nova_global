from django.shortcuts import render

def home(request):
    return render(request, 'nova_global/home.html')