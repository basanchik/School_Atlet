from django.db import models


class About(models.Model):
    ShortNameOrg = models.CharField('Сокращенное наименование вашей организации', max_length=60, unique=True)
    LongNameOrg = models.CharField('Полное наименование вашей организации', max_length=128, unique=True)
    DateCreator = models.CharField('Дата создания вашей организации', max_length=30)
    MinSport = models.CharField('Ваши учредители', max_length=60, unique=True)
    Filials = models.CharField('Ваши филиалы', max_length=60, unique=True)
    GeoPosition = models.CharField('Ваш адрес', max_length=300)
    GraFik = models.CharField('Ваш график работы', max_length=300)
    ContactPhone = models.TextField('Ваши номера телефонов', max_length=300)
    EmailAdress = models.CharField('Ваши контактные адреса электронной почты', max_length=300)
    SiteAdress = models.CharField('Адреса сайтов ваших филиалов', max_length=300)
    Tren = models.TextField('Места осуществления образовательной деятельности', null=True, blank=True)
    TrenPhoto = models.ImageField('Фото места осуществления образовательной деятельности', upload_to='static/about_images', blank=True, default='static/gerb.png')

    class Meta:
        verbose_name = 'Информация об организации'
        verbose_name_plural = 'Информация об организации'


class Otdel(models.Model):
    nameOtdel = models.CharField('Название отдела', max_length=200)
    adressOtdel = models.TextField("Место нахождение отдела адрес, номер, почта отдела", null=True, blank=True)
    docsOtdel = models.FileField('Положения', upload_to='static/docs', blank=True, null=True, help_text='Необязательное поле. Вы можете оставить его пустым.')

    class Meta:
        verbose_name = 'Отдел организации'
        verbose_name_plural = 'Отделы организации'


class Sotrudnik(models.Model):
    nameSotr = models.TextField("ФИО сотрудника, должность сотрудника, почта, номер телефона", null=True, blank=True)
    otdel = models.ForeignKey(Otdel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Информация о сотруднике'
        verbose_name_plural = 'Информация о сотрудниках'


class Obraz(models.Model):
    nameObraz = models.CharField('Название образовательной программы ', max_length=200)

    class Meta:
        verbose_name = 'Образовательная программа'
        verbose_name_plural = 'Образовательные программы'


class elementsObraz(models.Model):
    formObuch = models.CharField("Форма обучения", max_length=200)
    normSrokObuch = models.TextField("Нормативный срок обучения", null=True, blank=True)
    srokAkreditObuch = models.TextField("Срок действия гос. аккредитации образовательной программы ", null=True, blank=True)
    languageObraz = models.CharField("Языки, на которых осуществляется образовательная программа", max_length=200)
    moduleObraz = models.TextField("учебные курсы, предусмотренные соответствующей образовательной программы", null=True, blank=True)
    praktikObraz = models.TextField("Практики, предусмотренные соответствующей образовательной программы", null=True, blank=True)
    distanceObraz = models.TextField("образовательной программы при реализации элек. обучения на дистанционном обучении", null=True, blank=True)
    uchebPlan = models.FileField("Учебный план образовательной программы'электронный документ'", upload_to='static/docs', blank=True, null=True, default=None)
    annatotionDis = models.FileField("об аннотации по рабочим программам", upload_to='static/docs', blank=True, null=True, default=None)
    calendarUcheb = models.FileField("Календарный учебный график", upload_to='static/docs', blank=True, null=True, default=None)
    metodDocs = models.FileField("о методических документах образ. процесса ", upload_to='static/docs', blank=True, null=True, default=None)
    obshislo = models.CharField("Общая численность обучающихся", max_length=100)
    obshisloBudgetFed = models.CharField("Общая численность обучающихся за счет федеральных бюджетных средств", max_length=100)
    obshisloBudgetReg = models.CharField("Общая численность обучающихся за счет бюджетных средств субъекта", max_length=100)
    obshisloBudgetSMO = models.CharField("Общая численность обучающихся за счет местных бюджетов", max_length=100)
    obshisloDogovor = models.CharField("Общая численность обучающихся по договору об образовании", max_length=100)
    Licenzy = models.FileField("Лицензия на осуществление образовательной деятельности", upload_to='static/docs', blank=True, null=True, default=None)
    nameObr = models.ForeignKey(Obraz, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Об образовательной программе'
        verbose_name_plural = 'Об образовательных программах'





