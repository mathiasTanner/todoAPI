from rest_framework import serializers
from todoList.models import List, Task

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model=List
        fields=('ListId', 'ListName')
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=('TaskId', 'TaskName', 'List', 'Deadline', 'Status')