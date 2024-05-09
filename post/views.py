from django.shortcuts import render ,HttpResponse
from .models import postt

# Create your views here.
def home(request):
    posts=postt.objects.all()
    return render(request ,'index.html',{'posts':posts})

def more(request,pk):
    more1=postt.objects.get(id=pk)
    return render(request ,'full.html',{'more1':more1})
