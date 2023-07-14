# Generated by Django 4.2 on 2023-06-20 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShortNameOrg', models.CharField(max_length=60, unique=True, verbose_name='Сокращенное наименование вашей организации')),
                ('LongNameOrg', models.CharField(max_length=128, unique=True, verbose_name='Полное наименование вашей организации')),
                ('DateCreator', models.CharField(max_length=30, verbose_name='Дата создания вашей организации')),
                ('MinSport', models.CharField(max_length=60, unique=True, verbose_name='Ваши учредители')),
                ('Filials', models.CharField(max_length=60, unique=True, verbose_name='Ваши филиалы')),
                ('GeoPosition', models.CharField(max_length=300, verbose_name='Ваш адрес')),
                ('GraFik', models.CharField(max_length=300, verbose_name='Ваш график работы')),
                ('ContactPhone', models.TextField(max_length=300, verbose_name='Ваши номера телефонов')),
                ('EmailAdress', models.CharField(max_length=300, verbose_name='Ваши контактные адреса электронной почты')),
                ('SiteAdress', models.CharField(max_length=300, verbose_name='Адреса сайтов ваших филиалов')),
                ('Tren', models.TextField(blank=True, null=True, verbose_name='Места осуществления образовательной деятельности')),
                ('TrenPhoto', models.ImageField(blank=True, default='static/gerb.png', upload_to='static/about_images', verbose_name='Фото места осуществления образовательной деятельности')),
            ],
            options={
                'verbose_name': 'Информация об организации',
                'verbose_name_plural': 'Информация об организации',
            },
        ),
        migrations.CreateModel(
            name='Otdel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOtdel', models.CharField(max_length=200, verbose_name='Название отдела')),
                ('adressOtdel', models.TextField(blank=True, null=True, verbose_name='Место нахождение отдела адрес, номер, почта отдела')),
                ('docsOtdel', models.FileField(blank=True, default=None, null=True, upload_to='static/docs', verbose_name='Положения')),
            ],
            options={
                'verbose_name': 'Отдел организации',
                'verbose_name_plural': 'Отделы организации',
            },
        ),
        migrations.CreateModel(
            name='Sotrudnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameSotr', models.TextField(blank=True, null=True, verbose_name='ФИО сотрудника, должность сотрудника, почта, номер телефона')),
                ('otdel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.otdel')),
            ],
            options={
                'verbose_name': 'Информация о сотруднике',
                'verbose_name_plural': 'Информация о сотрудниках',
            },
        ),
    ]