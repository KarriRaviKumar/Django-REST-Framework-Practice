from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.EmployeeViewSet,basename='employee')

urlpatterns = [
    path('students/',views.studentview),
    path('students/<int:pk>',views.student_info),

    # path('employees/',views.Employee.as_view()),
    # path('employees/<int:pk>',views.EmployeeDetail.as_view()),
    path('',include(router.urls)),

    path('blogs/',views.Blogs.as_view()),
    path('comments/',views.Comment.as_view()),

    path('blogs/<int:pk>/',views.BlogDetail.as_view()),
    path('comments/<int:pk>/',views.CommentDetail.as_view()),
]