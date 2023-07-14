from django.db import models


class EducationalResources(models.Model):
    equipped_classrooms = models.TextField(verbose_name='Оборудованные учебные кабинеты', null=True, blank=True)
    practical_training_facilities = models.TextField(verbose_name='Объекты для проведения практических занятий', null=True, blank=True)
    libraries = models.TextField(verbose_name='Библиотека(и)', null=True, blank=True)
    sports_facilities = models.TextField(verbose_name='Объекты спорта', null=True, blank=True)
    teaching_aids = models.TextField(verbose_name='Средства обучения и воспитания', null=True, blank=True)
    student_meals = models.TextField(verbose_name='Условия питания обучающихся', null=True, blank=True)
    student_healthcare = models.TextField(verbose_name='Условия охраны здоровья обучающихся', null=True, blank=True)
    information_systems_access = models.TextField(verbose_name='Доступ к информационным системам и информационно-телекоммуникационным сетям', null=True, blank=True)
    own_electronic_resources = models.TextField(verbose_name='Собственные электронные образовательные и информационные ресурсы', null=True, blank=True)
    external_electronic_resources = models.TextField(verbose_name='Сторонние электронные образовательные и информационные ресурсы', null=True, blank=True)

    class Meta:
        verbose_name = 'Материально-техническое обеспечение и оснащенность образовательного процесса'
        verbose_name_plural = 'Материально-техническое обеспечение и оснащенность образовательного процесса'

    def __str__(self):
        return self.verbose_name


class Support(models.Model):
    information = models.TextField(null=True, blank=True, verbose_name='Информация о стипендиях и мерах поддержки обучающихся')
    scholarships = models.TextField(null=True, blank=True, verbose_name='О наличии и условиях предоставления стипендий')
    social_support = models.TextField(null=True, blank=True, verbose_name='О мерах социальной поддержки')
    dormitory = models.TextField(null=True, blank=True, verbose_name='О наличии общежития, интерната')
    accommodation = models.TextField(null=True, blank=True, verbose_name='О количестве жилых помещений в общежитии, интернате для иногородних обучающихся')
    accommodation_payment = models.TextField(null=True, blank=True, verbose_name='О формировании платы за проживание в общежитии')
    employment = models.TextField(null=True, blank=True, verbose_name='О трудоустройстве выпускников, с указанием численности трудоустроенных выпускников от общей численности выпускников в прошедшем учебном году, для каждой реализуемой образовательной программы, по которой состоялся выпуск')

    class Meta:
        verbose_name = 'Страница стипендий и мер поддержки обучающихся'
        verbose_name_plural = 'Страницы стипендий и мер поддержки обучающихся'

    def __str__(self):
        return self.information


class PaidEducationService(models.Model):
    order_of_services = models.TextField(verbose_name="Порядок оказания платных образовательных услуг", null=True, blank=True)
    contract_sample = models.FileField(verbose_name="Образец договора об оказании платных образовательных услуг", upload_to='static/docs', blank=True, null=True)
    tuition_cost = models.TextField(verbose_name="Стоимость обучения по каждой образовательной программе", null=True, blank=True)
    payment_amount = models.TextField(verbose_name="Размер платы за присмотр и уход за детьми", null=True, blank=True)

    class Meta:
        verbose_name = "Платная образовательная услуга"
        verbose_name_plural = "Платные образовательные услуги"