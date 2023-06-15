from django.shortcuts import render

# Create your views here.
def filter(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'ThIs iS DjAnGo Class','dt':dt}
    return render(request,'filter.html',d)