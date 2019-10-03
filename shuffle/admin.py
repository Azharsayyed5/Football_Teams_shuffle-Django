from django.contrib import admin
from shuffle.models import Teams

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display=('id','imageurl','Tname')

admin.site.register(Teams,TeamAdmin)


