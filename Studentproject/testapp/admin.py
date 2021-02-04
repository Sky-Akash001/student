from django.contrib import admin
from testapp.models import Studentregister

class StudentAdmin(admin.ModelAdmin):
    list_display=["name","marks"]
admin.site.register(Studentregister,StudentAdmin)
