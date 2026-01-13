
from django.urls import path,include
from . import views

urlpatterns = {
    path('Chaye/',views.all_chai,name='all'),
}

