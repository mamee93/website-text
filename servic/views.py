from django.shortcuts import render
from .models import  Services
# Create your views here.

def post_services(request):
    all_services = Services.objects.all()
    return render(request,'servic/list_services.html',{'all_services':all_services})


