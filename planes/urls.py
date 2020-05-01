from django.urls import path
from planes import views


app_name = 'planes'

urlpatterns = [
    path('<int:curator_id>/cqc_save', views.cqc_save, name='cqc_save'),
    path('<int:curator_id>/edit', views.edit_cqc, name='cqc_edit'),
    path('<int:finance_cost_id>/', views.show_all_curator),
    path('<int:finance_cost_id>/add/', views.add_curator, name = 'add'),
    path('<int:finance_cost_id>/save/', views.save_curator, name='save'),
    path('', views.plane),

]
