# Generated by Django 4.2 on 2023-07-10 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalResources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipped_classrooms', models.TextField(blank=True, null=True, verbose_name='Оборудованные учебные кабинеты')),
                ('practical_training_facilities', models.TextField(blank=True, null=True, verbose_name='Объекты для проведения практических занятий')),
                ('libraries', models.TextField(blank=True, null=True, verbose_name='Библиотека(и)')),
                ('sports_facilities', models.TextField(blank=True, null=True, verbose_name='Объекты спорта')),
                ('teaching_aids', models.TextField(blank=True, null=True, verbose_name='Средства обучения и воспитания')),
                ('student_meals', models.TextField(blank=True, null=True, verbose_name='Условия питания обучающихся')),
                ('student_healthcare', models.TextField(blank=True, null=True, verbose_name='Условия охраны здоровья обучающихся')),
                ('information_systems_access', models.TextField(blank=True, null=True, verbose_name='Доступ к информационным системам и информационно-телекоммуникационным сетям')),
                ('own_electronic_resources', models.TextField(blank=True, null=True, verbose_name='Собственные электронные образовательные и информационные ресурсы')),
                ('external_electronic_resources', models.TextField(blank=True, null=True, verbose_name='Сторонние электронные образовательные и информационные ресурсы')),
            ],
            options={
                'verbose_name': 'Материально-техническое обеспечение и оснащенность образовательного процесса',
                'verbose_name_plural': 'Материально-техническое обеспечение и оснащенность образовательного процесса',
            },
        ),
        migrations.CreateModel(
            name='PaidEducationService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_of_services', models.TextField(blank=True, null=True, verbose_name='Порядок оказания платных образовательных услуг')),
                ('contract_sample', models.FileField(blank=True, null=True, upload_to='static/docs', verbose_name='Образец договора об оказании платных образовательных услуг')),
                ('tuition_cost', models.TextField(blank=True, null=True, verbose_name='Стоимость обучения по каждой образовательной программе')),
                ('payment_amount', models.TextField(blank=True, null=True, verbose_name='Размер платы за присмотр и уход за детьми')),
            ],
            options={
                'verbose_name': 'Платная образовательная услуга',
                'verbose_name_plural': 'Платные образовательные услуги',
            },
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information', models.TextField(blank=True, null=True, verbose_name='Информация о стипендиях и мерах поддержки обучающихся')),
                ('scholarships', models.TextField(blank=True, null=True, verbose_name='О наличии и условиях предоставления стипендий')),
                ('social_support', models.TextField(blank=True, null=True, verbose_name='О мерах социальной поддержки')),
                ('dormitory', models.TextField(blank=True, null=True, verbose_name='О наличии общежития, интерната')),
                ('accommodation', models.TextField(blank=True, null=True, verbose_name='О количестве жилых помещений в общежитии, интернате для иногородних обучающихся')),
                ('accommodation_payment', models.TextField(blank=True, null=True, verbose_name='О формировании платы за проживание в общежитии')),
                ('employment', models.TextField(blank=True, null=True, verbose_name='О трудоустройстве выпускников, с указанием численности трудоустроенных выпускников от общей численности выпускников в прошедшем учебном году, для каждой реализуемой образовательной программы, по которой состоялся выпуск')),
            ],
            options={
                'verbose_name': 'Страница стипендий и мер поддержки обучающихся',
                'verbose_name_plural': 'Страницы стипендий и мер поддержки обучающихся',
            },
        ),
    ]
