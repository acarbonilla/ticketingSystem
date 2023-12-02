from django.urls import path
from staff.views import staff, openTicket, sdINC, sdSR, closedTicket
from staff.viewer.viewsmonth2023 import july, august, september, october, november, december

urlpatterns = [
    path('', staff, name='staff'),
    path('openTicket/', openTicket, name='openTicket'),

    # Paginator. closeTicket is June
    path('closedTicket/', closedTicket, name='closedTicket'),
    path('july/', july, name='july'),
    path('august/', august, name='august'),
    path('september/', september, name='september'),
    path('october/', october, name='october'),
    path('november/', november, name='november'),
    path('december/', december, name='december'),


    # Edit
    path('sdINC/<str:pk>', sdINC, name='sdINC'),
    path('sdSR/<str:pk>', sdSR, name='sdSR'),
]
