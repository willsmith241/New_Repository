from django.urls import path
from .import views

urlpatterns =[
    path('profile/',views.Profile_create,name='profiles'),
    path('profilelist/',views.ProfileList,name='profilelist'),
    path('',views.home,name='home'),
    path('portfolio/',views.Portfolio,name='portfolio'),
    path('about/',views.about,name='about'),


]
