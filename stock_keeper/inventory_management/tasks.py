from celery import shared_task
from .models import Shelf, InventoryManagementTask


@shared_task
def calculate_total_weight_on_shelves(task_id):
    task = InventoryManagementTask.objects.get(id = task_id)
    task.task_status = "PARSING"
    task.save()
    total_weight = 0
    shelves = Shelf.objects.all()
    for shelf in shelves:
        total_weight += shelf.current_quantity
    task.task_status = "OK"
    task.result["answer"] = total_weight
    task.save()
