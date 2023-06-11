from rest_framework import mixins, viewsets
from rest_framework import permissions
from . import serializers
from .filters import EmployeesFilter
from .models import Department, Employee
from .paginator import StandardResultsSetPagination


class DepartmentsViewSet(mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
        A simple ViewSet for viewing departments.
    """
    queryset = Department.objects.all()
    serializer_class = serializers.DepartamentSerializer
    permission_classes = [permissions.AllowAny]


class EmployeesViewSet(mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    """
        A simple ViewSet for viewing employees.
    """
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filterset_class = EmployeesFilter
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.IsAuthenticated]

