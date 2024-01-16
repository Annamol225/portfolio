from . import views
from django.urls import path


urlpatterns = [
     path('',views.index,name='index'),
     path('contact',views.query1,name='contact'),
     path('blog',views.blog,name='blog'),
     
]