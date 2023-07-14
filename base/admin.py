from django.contrib import admin

from base.models import About, Sotrudnik, Otdel, Obraz, elementsObraz


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'LongNameOrg')


class elementsObrazAdmin(admin.ModelAdmin):
    list_display = ('id', 'nameObr')


class SotrudnikAdmin(admin.ModelAdmin):
    list_display = ('id', 'nameSotr')


class OtdelAdmin(admin.ModelAdmin):
    list_display = ('id', 'nameOtdel')


class ObrazAdmin(admin.ModelAdmin):
    list_display = ('id', 'nameObraz')


admin.site.register(About, AboutAdmin)
admin.site.register(Sotrudnik, SotrudnikAdmin)
admin.site.register(Otdel, OtdelAdmin)
admin.site.register(Obraz, ObrazAdmin)
admin.site.register(elementsObraz, elementsObrazAdmin)