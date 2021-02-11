from django.conf.urls import url
from django.urls import path, include
from user_account import views

urlpatterns = [
    # path('register/',views.register,name='register'),
    # path('register/<str:code>',views.register,name='register'),
    path('',views.landing,name='landing'),]