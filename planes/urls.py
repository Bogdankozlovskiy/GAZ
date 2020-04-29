from django.urls import path
from planes import views


urlpatterns = [
    path('<int:finance_cost_id>/', views.show_all_curator),
    path('', views.plane),

]
