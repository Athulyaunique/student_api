from django.contrib import admin
from.models import Student

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display=('id','name','age','email','entrollment_date')
    list_filter=('age',)
    search_fields=('name','email')
admin.site.register(Student,studentAdmin)