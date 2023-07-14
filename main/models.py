from django.db import models


class News(models.Model):
    name = models.CharField('Название',max_length=128, unique=True)
    image = models.ImageField('Картинка', upload_to='static/news_images', blank=True, default='static/gerb.png')
    text = models.TextField('Текст новости', null=True, blank=True)
    date = models.DateTimeField('Время', auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Document(models.Model):
    nameDocs = models.CharField('Название документа', max_length=300)
    docs = models.FileField('Файл', upload_to='static/docs', blank=True, null=True, default=None)
    dateDocs = models.DateTimeField('Время', auto_now_add=True)


    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'