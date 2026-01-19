from django.shortcuts import render
from .models import Chaivarity


# Create your views here.

def all_chai(request):
    chais=Chaivarity.objects.all()   ##just extract object to see values  of database.since u r using ORM
    return render(request, 'Chaye/all_Chaye.html',{'chais':chais})
