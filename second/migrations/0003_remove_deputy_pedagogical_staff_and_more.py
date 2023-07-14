# Generated by Django 4.2 on 2023-07-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0002_alter_pedagogicalstaff_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deputy',
            name='pedagogical_staff',
        ),
        migrations.RemoveField(
            model_name='educationalstaff',
            name='pedagogical_staff',
        ),
        migrations.AlterModelOptions(
            name='pedagogicalstaff',
            options={'verbose_name_plural': 'Структура'},
        ),
        migrations.RemoveField(
            model_name='pedagogicalstaff',
            name='contact_phone',
        ),
        migrations.RemoveField(
            model_name='pedagogicalstaff',
            name='email',
        ),
        migrations.RemoveField(
            model_name='pedagogicalstaff',
            name='first_name',
        ),
        migrations.AddField(
            model_name='pedagogicalstaff',
            name='image',
            field=models.ImageField(blank=True, default='static/gerb.png', upload_to='static/news_images', verbose_name='Изображение структуры организации'),
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='Deputy',
        ),
        migrations.DeleteModel(
            name='EducationalStaff',
        ),
    ]
