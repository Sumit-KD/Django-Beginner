from django import forms
from .models import Chaivarity

class ChaiVarityForm(forms.Form):
    chai_varity=forms.ModelChoiceField(queryset=Chaivarity.objects.all(),label="Select Chai Varity")

    #ModelChoiceField--> it will automatically made choice acc, to the request made by client
    #object.all()--> sapai objects hru lai ChaiVarity relation bata nikalxa



