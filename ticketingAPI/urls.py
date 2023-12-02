from django.urls import path
from .views import snippet_list, snippet_detail, incidentTicket, serviceTicket, inc_detail, posting

urlpatterns = [
    path('snippet_list/', snippet_list),
    path('snippet_detail/<int:pk>', snippet_detail),

    # This is for showing the total ticket within the months.
    path('', incidentTicket),
    path('srticket/', serviceTicket),

    # For editing, details, delete
    path('inc_detail/<str:pk>', inc_detail),

    # for posting
    path('posting/', posting),
]
