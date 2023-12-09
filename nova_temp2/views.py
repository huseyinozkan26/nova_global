from django.shortcuts import render,HttpResponse

def home(request):
    #return HttpResponse("bla bla")
    return render(request, 'nova_temp2/home.html')