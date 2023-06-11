from django.contrib import admin
from .models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "director"]

    def get_form(self, request, obj=None, **kwargs):
        form = super(DepartmentAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['director'].queryset = Employee.objects.filter(position='Дир')
        return form


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["full_name", "position", "department"]
    list_filter = ["position", "department__name"]
