from django.shortcuts import render

from four.models import FinancialActivity, FinancialSummary, FinancialPlan


def Economy(request):
    money = {
        'mon': FinancialActivity.objects.order_by()[:],
        'mon2': FinancialSummary.objects.order_by()[:],
        'mon3': FinancialPlan.objects.order_by()[:]
    }
    return render(request, 'main/Economy.html', money)


