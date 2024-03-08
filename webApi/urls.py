from django.urls import path, include
from .views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', viewset=CompanyViewSet)
router.register(r'employees', viewset=EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]