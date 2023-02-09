from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from .serializers import DepartmentViewSet, EmployeeViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'department', DepartmentViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url('employee/', views.employee_detail, name='employee'),
    url('employee/<pk>/', views.employee_detail,name='employee-detail'),
    url('department/', views.department_detail, name='department'),
    url('department/<pk>', views.department_detail,name='department-detail'),
]
