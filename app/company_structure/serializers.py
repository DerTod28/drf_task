from django.db import IntegrityError
from django.db.models import Sum
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Department, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        try:
            return super().create(validated_data)

        except IntegrityError as error:
            raise ValidationError from error


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
