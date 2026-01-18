from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),   # admin should ALWAYS be here::usernmae:Sumit and PD-->@sum11
    path('', views.home, name='home'), # homepage
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('Chaye/', include('Chaye.urls') ),

    path("__reload__/", include("django_browser_reload.urls")),  # setup for hot reloading
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

