from django.urls import path
from codingsession import views

urlpatterns = [
    path('', views.codingsessionspage, name='codingsessionspage'),
]
