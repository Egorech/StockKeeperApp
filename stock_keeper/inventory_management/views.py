from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from inventory_management.serializer import ShelfSerializer
from inventory_management.tasks import *


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def update_shelf_quantity(request):
    if request.method == 'GET':
        shelves = Shelf.objects.all()
        serializer = ShelfSerializer(shelves, many = True)
        return Response(serializer.data)

    data = request.data
    if 'shelf_id' not in data or 'quantity' not in data or 'method' not in data:
        return Response({'error': 'Required fields shelf_id, quantity, and method are missing in the request data'},
                        status = 400)

    shelf_id = data['shelf_id']
    quantity = int(data['quantity'])
    method = data['method']

    try:
        shelf = Shelf.objects.get(id = shelf_id)
    except Shelf.DoesNotExist:
        return Response({'error': 'Shelf with the specified ID does not exist'}, status = 404)

    if method == '+':
        total_weight = sum([s.current_quantity for s in Shelf.objects.filter(location = shelf.location)])

        if (total_weight + quantity) > shelf.location.max_weight_capacity:
            return Response({'error': 'Total weight of shelves in the location '
                                      'exceeds the maximum capacity of the storage location'},
                            status = 400)
        shelf.current_quantity += quantity
        shelf.save()
    elif method == '-':
        if shelf.current_quantity < quantity:
            return Response({'error': 'Cannot extract more quantity than available on the shelf'}, status = 400)
        shelf.current_quantity -= quantity
        shelf.save()
    else:
        return Response({'error': 'Invalid method. Use either "+" for addition or "-" for extraction'},
                        status = 400)
    return Response({'message': 'Quantity updated on the shelf successfully'})


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def create_calculate_total_weight_task(request):
    if request.method == 'GET':
        response = {
            "Possible statuses:":
                {
                    "WAITING": "ожидание обработки",
                    "PARSING ": "данные в процессе обработки",
                    "OK": "завершено",
                }
        }
        return Response(response)

    task = InventoryManagementTask.objects.create(user = request.user)

    # celery task
    calculate_total_weight_on_shelves.delay(task.id)

    return Response({'task_id': task.id})


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def task_result(request, task_id):
    user = request.user
    try:
        task = InventoryManagementTask.objects.get(id = task_id)
    except InventoryManagementTask.DoesNotExist:
        raise NotFound('No such task_id')
    if user != task.user and not user.is_superuser:
        raise PermissionDenied('This task is not yours')
    if task.task_status == 'OK':
        return Response({'succes': task.result, 'status': task.task_status})
    else:
        return Response({'status': task.task_status})
