from django.contrib import admin

from second.models import FedStandart, PedagogicalStaff


class AdminFedStandart(admin.ModelAdmin):
    list_dislay=('id', )


class AdminPedagogicalStaff(admin.ModelAdmin):
    list_dislay=('first_name',"last_name", 'middle_name')


admin.site.register(FedStandart, AdminFedStandart)
admin.site.register(PedagogicalStaff, AdminPedagogicalStaff)
