from django.db import models
from django.conf import settings
import random


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    surname = models.CharField(verbose_name="Фамилия", max_length=25)
    name = models.CharField(verbose_name="Имя", max_length=25)
    patronymic = models.CharField(verbose_name="Отчество", max_length=25)

    friends = models.ForeignKey(settings.AUTH_USER_MODEL,related_name ="friends", verbose_name="Список друзей", on_delete=models.CASCADE)
    black_sheet = models.ForeignKey(settings.AUTH_USER_MODEL, related_name ="black_sheet",verbose_name="Список врагов", on_delete=models.CASCADE)


    # TODO пользователь только в одном из полей

    r_link = random.randint(123456789111, 999999999999)
    r_link = str(r_link)
    link = models.CharField(verbose_name="Сылка", default=r_link, max_length=25, unique=True)
    img_caver = models.ImageField(verbose_name="Кавер")
    img_avatar = models.ImageField(verbose_name="Аватарка")

    def __str__(self):
        string = f"{self.id} - {self.surname} {self.name} {self.patronymic}"
        return string

    class Meta():
        ordering = ('-id',)
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class Room_comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200,verbose_name ="Комментарий")
    date = models.DateTimeField(auto_now_add=True,verbose_name ="Дата/время")

    def __str__(self):
        string = f"{self.id} - {self.user}"
        return string

    class Meta():
        ordering = ('-id',)
        verbose_name = 'Комментарии в диалогах'
        verbose_name_plural = 'Комментарии в диалогах'


class Rom(models.Model):
    user_main = models.OneToOneField(settings.AUTH_USER_MODEL,verbose_name ="Создатель",related_name ="user_main", on_delete=models.CASCADE)
    user_invited = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name ="Гости",related_name ="user_invited", on_delete=models.CASCADE)
    name = models.CharField(max_length=50,verbose_name ="Название комноты")
    comment = models.ForeignKey(Room_comment,on_delete=models.CASCADE,verbose_name ="Комментарий")

    def __str__(self):
        string = f"{self.id} - {self.name}"
        return string

    class Meta():
        ordering = ('-id',)

        verbose_name = 'Диалоги пользователей'
        verbose_name_plural = 'Диалоги пользователей'