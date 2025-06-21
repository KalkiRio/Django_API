from rest_framework import serializers
from .models import Task, Category
from accounts.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

class TaskSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)
    assigned_to_id = serializers.IntegerField(write_only=True, required=False)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'priority', 'status', 'category',
            'category_name', 'assigned_to', 'assigned_to_id', 'created_by',
            'due_date', 'completed_at', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        if 'assigned_to_id' not in validated_data:
            validated_data['assigned_to'] = self.context['request'].user
        return super().create(validated_data)

class TaskCreateSerializer(serializers.ModelSerializer):
    assigned_to_id = serializers.IntegerField(required=False)

    class Meta:
        model = Task
        fields = [
            'title', 'description', 'priority', 'status', 'category',
            'assigned_to_id', 'due_date'
        ]

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        if 'assigned_to_id' not in validated_data:
            validated_data['assigned_to'] = self.context['request'].user
        return super().create(validated_data)
