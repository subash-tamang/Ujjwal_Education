from django.contrib import admin
from .models import School

# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(School, SchoolAdmin)
