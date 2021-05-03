from cls.models import  Degree, Employ, Training, Vacation, Attendance
from django.contrib import admin

# Register your models here.

    
class EmployAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['name','phonenumber','salary','Email','address','Degree']
class VacationAdmin(admin.ModelAdmin):
    list_display=['employ_name','title','start_date','end_date']
class AttendanceAdmin(admin.ModelAdmin):
     list_display=['name_employ','status','date']

class TrainingAdmin(admin.ModelAdmin):
    list_display=['names','title','description']   
admin.site.register(Employ, EmployAdmin)
admin.site.register(Degree)
admin.site.register(Attendance,AttendanceAdmin)
admin.site.register(Vacation,VacationAdmin)
admin.site.register(Training,TrainingAdmin)