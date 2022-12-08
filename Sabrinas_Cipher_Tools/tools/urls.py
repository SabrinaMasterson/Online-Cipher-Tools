from django.urls import path
from . import views

urlpatterns = [
    path('tools/', views.tools_home),
    path('passdict/', views.password_dictionary),
    path('ciphencode/', views.cipher_encoding),
]
