from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('photographer', views.photographer, name='photographer'),
    path('top_Photographers', views.top_photographers, name='top_Photographers'),
    path('regulations', views.regulations, name='regulations'),
    path('contacts', views.contacts, name='contacts'),
    path('donation', views.donation, name='donation'),
    # path('about-a', views.about)



]