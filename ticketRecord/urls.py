from django.urls import path
from ticketRecord.views import *


urlpatterns = [
    path('recordINC/', recordINC, name='recordINC'),
    path('recordSR/', recordSR, name='recordSR'),
]

