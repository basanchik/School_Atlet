# Generated by Django 4.2 on 2023-07-08 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_elementsobraz_obraz'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementsobraz',
            name='nameObr',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.obraz'),
            preserve_default=False,
        ),
    ]
