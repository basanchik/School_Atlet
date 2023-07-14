from django.db import models


class FinancialActivity(models.Model):
    period = models.TextField(null=True, blank=True, verbose_name='отчетный период')
    budget_federal = models.FileField(verbose_name='Бюджетные ассигнования федерального бюджета', upload_to='static/docs', blank=True, null=True)
    budget_regional = models.FileField(verbose_name='Бюджеты субъектов Российской Федерации', upload_to='static/docs', blank=True, null=True)
    budget_local = models.FileField(verbose_name='Местные бюджеты', upload_to='static/docs', blank=True, null=True)
    paid_services = models.FileField(verbose_name='Договоры об оказании платных образовательных услуг', upload_to='static/docs', blank=True, null=True)

    class Meta:
        verbose_name = 'Финансово-хозяйственная деятельность'
        verbose_name_plural = 'Финансово-хозяйственная деятельность'

    def __str__(self):
        return f'Финансово-хозяйственная деятельность: {self.subsection.title}'


class FinancialSummary(models.Model):
    period = models.TextField(null=True, blank=True, verbose_name='отчетный период')
    financial_year = models.PositiveIntegerField(verbose_name='Финансовый год')
    incoming_funds = models.FileField(verbose_name='Поступление финансовых и материальных средств', upload_to='static/docs', blank=True, null=True)
    outgoing_funds = models.FileField(verbose_name='Расходование финансовых и материальных средств', upload_to='static/docs', blank=True, null=True)

    class Meta:
        verbose_name = 'Финансовая сводка'
        verbose_name_plural = 'Финансовые сводки'

    def __str__(self):
        return f'Финансовая сводка: {self.subsection.title} - {self.financial_year}'


class FinancialPlan(models.Model):
    period = models.TextField(null=True, blank=True, verbose_name='отчетный период')
    financial_plan = models.FileField(verbose_name='План финансово-хозяйственной деятельности', upload_to='static/docs', blank=True, null=True)

    class Meta:
        verbose_name = 'Финансовый план'
        verbose_name_plural = 'Финансовые планы'

    def __str__(self):
        return f'Финансовый план: {self.subsection.title}'