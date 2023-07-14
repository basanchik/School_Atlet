# Generated by Django 4.2 on 2023-07-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.TextField(blank=True, null=True, verbose_name='отчетный период')),
                ('budget_federal', models.FileField(blank=True, null=True, upload_to='static/docs', verbose_name='Бюджетные ассигнования федерального бюджета')),
                ('budget_regional', models.FileField(blank=True, null=True, upload_to='static/docs', verbose_name='Бюджеты субъектов Российской Федерации')),
                ('budget_local', models.FileField(blank=True, null=True, upload_to='static/docs', verbose_name='Местные бюджеты')),
                ('paid_services', models.FileField(blank=True, null=True, upload_to='static/docs', verbose_name='Договоры об оказании платных образовательных услуг')),
            ],
            options={
                'verbose_name': 'Финансово-хозяйственная деятельность',
                'verbose_name_plural': 'Финансово-хозяйственная деятельность',
            },
        ),
        migrations.CreateModel(
            name='FinancialPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.TextField(blank=True, null=True, verbose_name='отчетный период')),
                ('financial_plan', models.FileField(blank=True, null=True, upload_to='static/docs', verbose_name='План финансово-хозяйственной деятельности')),
            ],
            options={
                'verbose_name': 'Финансовый план',
                'verbose_name_plural': 'Финансовые планы',
            },
        ),
        migrations.CreateModel(
            name='FinancialSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.TextField(blank=True, null=True, verbose_name='отчетный период')),
                ('financial_year', models.PositiveIntegerField(verbose_name='Финансовый год')),
                ('incoming_funds', models.FileField(blank=True, null=True, upload_to='static/docs', verbose_name='Поступление финансовых и материальных средств')),
                ('outgoing_funds', models.FileField(blank=True, null=True, upload_to='static/docs', verbose_name='Расходование финансовых и материальных средств')),
            ],
            options={
                'verbose_name': 'Финансовая сводка',
                'verbose_name_plural': 'Финансовые сводки',
            },
        ),
    ]
