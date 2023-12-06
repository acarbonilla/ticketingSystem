from django.urls import path
from . import views


urlpatterns = [
    path('memberLogin/', views.memberLogin, name='memberlogin'),
    path('sflogout', views.sflogout, name='sflogout'),

]