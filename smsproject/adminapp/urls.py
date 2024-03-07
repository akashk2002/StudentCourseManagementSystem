from django.urls import path
from . import views

urlpatterns = [
    path("adminhome",views.adminhome,name='adminhome'),
    path("adminlogout",views.logout,name='adminlogout')
]