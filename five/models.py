from django.db import models


class VacantSeat(models.Model):
    program = models.CharField(max_length=100, null=True, blank=True, verbose_name='Реализуемая образовательная программа')
    specialty = models.CharField(max_length=100, null=True, blank=True, verbose_name='Реализуемая специальность')
    training_direction = models.CharField(max_length=100, null=True, blank=True, verbose_name='Реализуемое направление подготовки')
    scientific_specialty = models.CharField(max_length=100, null=True, blank=True, verbose_name='Научная специальность')
    profession = models.CharField(max_length=100, null=True, blank=True, verbose_name='Реализуемая профессия')
    federal_budget_seats = models.IntegerField(null=True, blank=True, verbose_name='Количество вакантных мест за счёт бюджетных ассигнований федерального бюджета')
    regional_budget_seats = models.IntegerField(null=True, blank=True, verbose_name='Количество вакантных мест за счёт бюджетных ассигнований бюджетов субъекта Российской Федерации')
    local_budget_seats = models.IntegerField(null=True, blank=True, verbose_name='Количество вакантных мест за счёт бюджетных ассигнований местных бюджетов')
    private_seats = models.IntegerField(null=True, blank=True, verbose_name='Количество вакантных мест за счёт средств физических и (или) юридических лиц')

    class Meta:
        verbose_name = 'Вакантное место'
        verbose_name_plural = 'Вакантные места'

    def __str__(self):
        # Вербозное название для модели
        return f'{self.program} ({self.specialty})'


class EducationalOrganization(models.Model):
    special_equipped_classrooms = models.CharField(verbose_name='Специально оборудованные учебные кабинеты', max_length=300, blank=True, null=True, default=None)
    practical_training_facilities = models.CharField(verbose_name='Объекты для проведения практических занятий', max_length=300, blank=True, null=True, default=None)
    libraries = models.CharField(verbose_name='Библиотеки', max_length=300, blank=True, null=True, default=None)
    sports_facilities = models.CharField(verbose_name='Объекты спорта', max_length=300, blank=True, null=True, default=None)
    educational_resources = models.CharField(verbose_name='Средства обучения и воспитания', max_length=300, blank=True, null=True, default=None)
    accessible_buildings = models.FileField(verbose_name='Беспрепятственный доступ в здания образовательной организации', upload_to='static/docs', blank=True, null=True, default=None)
    special_dietary_requirements = models.TextField(verbose_name='Специальные условия питания', blank=True, null=True)
    electronic_resources_accessibility = models.CharField(verbose_name='Доступность электронных образовательных ресурсов', max_length=300, blank=True, null=True, default=None)
    special_technical_learning_tools = models.CharField(verbose_name='Специальные технические средства обучения', max_length=300, blank=True, null=True, default=None)
    dormitory_accessible_conditions = models.CharField(verbose_name='Условия беспрепятственного доступа в общежитие', max_length=300, blank=True, null=True, default=None)
    adapted_housing_units_in_dormitory = models.PositiveIntegerField(verbose_name='Количество жилых помещений для инвалидов в общежитии', blank=True, null=True)

    def __str__(self):
        return "Доступная среда"

    class Meta:
        verbose_name = "Доступная среда"


class SiteInformation(models.Model):
    agreements = models.TextField(verbose_name='Заключенные и планируемые договоры', blank=True, null=True)
    document = models.FileField(verbose_name='Документ', upload_to='static/docs', blank=True, null=True, default=None)
    accreditation = models.TextField(verbose_name='Международная аккредитация образовательных программ', blank=True, null=True)
    document2 = models.FileField(verbose_name='Документ', upload_to='static/docs', blank=True, null=True, default=None)

    def __str__(self):
        return "Международное сотрудничество"

    class Meta:
        verbose_name = "Международное сотрудничество"
