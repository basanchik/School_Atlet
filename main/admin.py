from django.contrib import admin

from main.models import News, Document


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'nameDocs')


admin.site.register(News, NewsAdmin)
admin.site.register(Document, DocumentAdmin)
