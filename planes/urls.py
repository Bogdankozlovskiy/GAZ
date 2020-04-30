from django.urls import path
from planes import views


app_name = 'planes'

urlpatterns = [
    path('<int:finance_cost_id>/', views.show_all_curator),
    path('<int:finance_cost_id>/add/', views.add_curator, name = 'add'),
    path('<int:finance_cost_id>/save/', views.save_curator, name='save'),
   
    path('', views.plane),

]
