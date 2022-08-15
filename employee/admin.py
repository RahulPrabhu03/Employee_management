from django.contrib import admin
from.models import Dependent, Employee,Role,Department

# Register your models here.

admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Dependent)


