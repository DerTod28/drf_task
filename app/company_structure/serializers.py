from django.db.models import Sum
from rest_framework import serializers
from .models import Department, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class DepartamentSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        employees = Employee.objects.filter(department__name=instance.name)
        representation['employees_number'] = employees.count()
        representation['employees_salary_sum'] = employees.aggregate(Sum('salary'))['salary__sum']
        return representation

    class Meta:
        model = Department
        fields = '__all__'
