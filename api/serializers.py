from rest_framework import serializers
from students.models import students
from employees.models import employee
from blogs.models import Blog,Comments

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
    comments = CommentSerializer(many=True,read_only=True)

