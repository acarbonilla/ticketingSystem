from django.urls import path
from baseApp.views import homeView, authView, incForm, srForm, incEditForm, srEditForm, incDetails, srDetails

urlpatterns = [
    path('', homeView, name='homeView'),
    path('authView/', authView, name='authView'),

    # Form
    path('incForm/', incForm, name='incForm'),
    path('srForm/', srForm, name='srForm'),

    # Edit Form
    path('incEditForm/<str:pk>/', incEditForm, name='incEditForm'),
    path('srEditForm/<str:pk>/', srEditForm, name='srEditForm'),

    # Details
    path('incDetails/<str:pk>/', incDetails, name='incDetails'),
    path('srDetails/<str:pk>/', srDetails, name='srDetails'),
]
