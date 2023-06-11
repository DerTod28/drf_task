import django_filters
from .models import Employee


class EmployeesFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(lookup_expr='icontains')

    department__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Employee
        fields = ['full_name', 'department']
