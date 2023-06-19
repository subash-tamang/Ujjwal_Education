from django.contrib import admin
from .models import School, Contact

# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name",)  # ("name",) -> "name" is name of the variable in School class/model ??


admin.site.register(School, SchoolAdmin)
admin.site.register(Contact)
