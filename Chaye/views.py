from django.shortcuts import render
from .models import Chaivarity
from django.shortcuts import get_object_or_404


# Create your views here.

def all_chai(request):
    chais=Chaivarity.objects.all()   ##just extract object to see values  of database.since u r using ORM
    return render(request, 'Chaye/all_Chaye.html',{'chais':chais})

def chai_details(request ,chai_id):
    chai=get_object_or_404(Chaivarity,pk=chai_id)
    return render(request,'Chaye/chai_detail.html',{'chai':chai})



