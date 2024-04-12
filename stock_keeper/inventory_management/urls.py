from django.urls import path
from .views import update_shelf_quantity, create_calculate_total_weight_task, task_result
urlpatterns = [
    path('', update_shelf_quantity),
    path('calculate_total_weight/', create_calculate_total_weight_task),
    path('calculate_total_weight/<int:task_id>/', task_result)
]