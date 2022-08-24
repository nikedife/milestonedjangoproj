from django.urls import path
from milehospital.views import index,about,element,contact,blog,video,service

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('element/',element,name='element'),
    path('contact/',contact,name='contact'),
    path('blog/',blog,name='blog'),
    path('service/',service,name='service'),
    path('video/', video, name='video'),

]