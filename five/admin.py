from django.contrib import admin

from five.models import VacantSeat, EducationalOrganization, SiteInformation


class VacantSeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'specialty')


class EducationalOrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'special_equipped_classrooms')


class SiteInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'agreements')


admin.site.register(VacantSeat, VacantSeatAdmin)
admin.site.register(EducationalOrganization, EducationalOrganizationAdmin)
admin.site.register(SiteInformation, SiteInformationAdmin)