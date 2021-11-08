# -*- coding: UTF-8 -*-

from django.db import models


class Clip(models.Model):
    title = models.CharField(max_length=50, verbose_name='Клип')
    content = models.TextField(null=True, blank= True, verbose_name='Описание')
    file = models.FileField(upload_to='clip', default='', max_length=255, verbose_name = 'Файл')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    cliptheme = models.ForeignKey('ClipTheme', null=True, on_delete=models.PROTECT, verbose_name='Тема')

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name_plural = 'Клипы'
        verbose_name = 'Клип'
        ordering = ['-published']

#
class ClipTheme(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Темы клипов'
        verbose_name = 'Тема клипа'
        ordering = ['name']

