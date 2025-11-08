from django.http import Http404, JsonResponse
from django.shortcuts import render
from students.models import students
from employees.models import employee
from blogs.models import Blog,Comments
from .serializers import StudentSerializer,EmployeeSerializer,BlogSerializer,CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins,generics,viewsets
from .paginations import CustomPagination
from employees.filter import EmployeeFilter
from rest_framework.filters import SearchFilter,OrderingFilter


#function based views
@api_view(['GET','POST'])
def studentview(request):
    if request.method == 'GET':
        student = students.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def student_info(request,pk):
    try:
        student = students.objects.get(pk=pk)
    except students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serilalizer = StudentSerializer(student)
        return Response(serilalizer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serilalizer = StudentSerializer(student,data=request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            return Response(serilalizer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''
- class based views using APIView
class Employee(APIView):
    def get(self,request):
        employees = employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeDetail(APIView):
    def get_object(self,pk):
        try:
            return employee.objects.get(pk=pk)
        except:
            raise Http404
        
    def get(self,request,pk):
        employees = self.get_object(pk)
        serializer = EmployeeSerializer(employees)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        employees = self.get_object(pk)
        serializer = EmployeeSerializer(employees,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        employees = self.get_object(pk)
        employees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

'''
class based views using mixins and generics 
class Employee(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    

class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)

'''

'''
#using generics
class Employee(generics.ListCreateAPIView):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
'''

# using Model view set
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    filterset_class = EmployeeFilter

class Blogs(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['blog_title','blog_body']
    ordering_fields = ['id']

class Comment(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'