from django.contrib import admin

from four.models import FinancialActivity, FinancialSummary, FinancialPlan


class AdminFinancialActivity(admin.ModelAdmin):
    list_dislay = ('id ', 'order_of_services')


class  AdminFinancialSummary(admin.ModelAdmin):
    list_dislay = ('id', 'information')


class AdminFinancialPlan(admin.ModelAdmin):
    list_dislay = ('id', 'equipped_classrooms')


admin.site.register(FinancialActivity, AdminFinancialActivity)
admin.site.register(FinancialSummary, AdminFinancialSummary)
admin.site.register(FinancialPlan, AdminFinancialPlan)