from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from todoList.models import List, Task
from todoList.serializers import ListSerializer, TaskSerializer
# Create your views here.


@csrf_exempt
def listApi(request, id=0):
    if request.method=='GET':
        lists = List.objects.all()
        lists_serializer = ListSerializer(lists, many=True)
        return JsonResponse(lists_serializer.data, safe=False)
    elif request.method=='POST':
        list_data=JSONParser().parse(request)
        lists_serializer = ListSerializer(data=list_data)
        if lists_serializer.is_valid():
            lists_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        list_data = JSONParser().parse(request)
        lst = List.objects.get(ListId=list_data['ListId'])
        lists_serializer=ListSerializer(lst, data=list_data)
        if lists_serializer.is_valid():
            lists_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        lst=List.objects.get(ListId=id)
        lst.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def taskApi(request, id=0):
    if request.method=='GET':
        tasks = Task.objects.all()
        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)
    elif request.method=='POST':
        task_data=JSONParser().parse(request)
        tasks_serializer = TaskSerializer(data=task_data)
        if tasks_serializer.is_valid():
            tasks_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        task_data = JSONParser().parse(request)
        task = Task.objects.get(TaskId=task_data['TaskId'])
        tasks_serializer=TaskSerializer(task, data=task_data)
        if tasks_serializer.is_valid():
            tasks_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        task=Task.objects.get(TaskId=id)
        task.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def taskByList(request, name):
    tasks = Task.objects.all().filter(List=name)
    tasks_serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(tasks_serializer.data, safe=False)
