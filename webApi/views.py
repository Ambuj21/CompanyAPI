from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Company, Employee
from rest_framework.decorators import action
from .Serializers import CompanySerializers, EmployeeSerializers


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers


    #api/company/{company_id}/{employee}


    @action(detail=True, methods=['get'])
    def employee(self, request, pk=None):
        company = Company.objects.get(pk=pk)
        emps = Employee.objects.filter(company=company)
        emps_serializer = EmployeeSerializers(emps, many=True, context={
            'request': request
        })
        return Response(emps_serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
