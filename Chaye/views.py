from django.shortcuts import render
from .models import Chaivarity,Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarityForm



# Create your views here.

def all_chai(request):
    chais=Chaivarity.objects.all()   ##just extract object to see values  of database.since u r using ORM
    return render(request, 'Chaye/all_Chaye.html',{'chais':chais})

def chai_details(request ,chai_id):
    chai=get_object_or_404(Chaivarity,pk=chai_id)
    return render(request,'Chaye/chai_detail.html',{'chai':chai})


def chai_store_view(request):
    stores = None  ##stores--> form submit vaisakepaxi frontent ma yo variable pass grne so that we can use it as instance odf obj. WHICH IS PASSED USING: {'stores':stores} in return section

    form = ChaiVarityForm()  ## default form for GET request

    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)  # stores post method data into form variable

        if form.is_valid():  ## to know the submitted form is valid or not
            chai_variety = form.cleaned_data['chai_varity']   ## chai_varity taken from forms.py / cleaned_data---> u want clean data

            ## working with store db now
            stores = Store.objects.filter(chai_varieties=chai_variety)


    return render(
        request,
        'Chaye/chai_stores.html',
        {'stores': stores, 'form': form}
    )









