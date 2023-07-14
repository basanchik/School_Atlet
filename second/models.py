from django.db import models


class FedStandart(models.Model):
    PrimenObrStandart = models.FileField("О применяемых государственных образовательных стандартах", upload_to='static/docs', blank=True, null=True, default=None)
    PrimenObrStandartText = models.TextField('Описание применяемых государственных образовательные стандарты', null=True, blank=True)
    UtverObrStandart = models.FileField("Об утвержденных государственных стандартах", upload_to='static/docs', blank=True, null=True, default=None)
    UtverObrStandartText = models.TextField('Описание утвержденных государственных стандартах', null=True, blank=True)

    class Meta:
        verbose_name = 'Об образовательных стандарте и требованиях'
        verbose_name_plural = 'Об образовательных стандарте и требованиях'


class PedagogicalStaff(models.Model):
    image = models.ImageField('Изображение структуры организации', upload_to='static/news_images', blank=True, default='static/gerb.png')

    class Meta:
        verbose_name_plural = 'Структура'

