from django.urls import path
from planes import views


urlpatterns = [
    path('', views.plane)
]
