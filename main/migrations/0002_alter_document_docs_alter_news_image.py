# Generated by Django 4.2 on 2023-05-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docs',
            field=models.FileField(blank=True, default=None, null=True, upload_to='static/docs', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, default='static/gerb.png', upload_to='static/news_images', verbose_name='Картинка'),
        ),
    ]