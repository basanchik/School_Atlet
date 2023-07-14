from django.contrib import admin

from three.models import PaidEducationService, Support, EducationalResources


class AdminPaidEducationService(admin.ModelAdmin):
    list_dislay = ('id ', 'order_of_services')


class  AdminSupport(admin.ModelAdmin):
    list_dislay = ('id', 'information')


class AdminEducationalResources(admin.ModelAdmin):
    list_dislay = ('id', 'equipped_classrooms')


admin.site.register(PaidEducationService, AdminPaidEducationService)
admin.site.register(Support, AdminSupport)
admin.site.register(EducationalResources, AdminEducationalResources)
