from django.contrib import admin
from .models import Employee , Intern , Address , Department
# Register your models here.

admin.site.register(Address)
admin.site.register(Department)

admin.site.register(Intern)

admin.site.register(Employee)