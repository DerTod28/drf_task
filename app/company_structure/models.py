from django.contrib.postgres.indexes import GinIndex
from django.db import models
from django.db.models import UniqueConstraint


class Department(models.Model):
    name = models.CharField(max_length=100)
    director = models.OneToOneField('Employee', on_delete=models.SET_NULL,
                                    null=True, blank=True, related_name='director')

    def __str__(self):
        return self.name


class Employee(models.Model):
    DIRECTOR = "Дир"
    EMPLOYEE = "Сотр"

    POSITION_CHOICES = [
        (DIRECTOR, "Директор"),
        (EMPLOYEE, "Сотрудник"),
    ]

    full_name = models.CharField(max_length=255, db_index=True)
    photo = models.ImageField(upload_to='employee_photos', null=True, blank=True)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES, default=EMPLOYEE,)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='department')

    class Meta:
        constraints = [
            UniqueConstraint(name='unique_fullname_department', fields=[
                'full_name', 'department'
            ])
        ]

        indexes = [
            GinIndex(fields=['full_name'], name='search_idx_employee'),
        ]

    def __str__(self):
        return self.full_name
