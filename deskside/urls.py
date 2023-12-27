from django.urls import path
from deskside.views import desksideView, deskINC, deskSR

urlpatterns = [
    path('desksideView/', desksideView, name='desksideView'),
    path('deskINC/<str:pk>', deskINC, name='deskINC'),
    path('deskSR/<str:pk>', deskSR, name='deskSR'),
]
