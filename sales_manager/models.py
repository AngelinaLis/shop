from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=124, db_index=True, verbose_name='Название')
    text = models.TextField(verbose_name='Описание', help_text='Введите описание книги')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    date_publish = models.DateField(auto_now_add=True, db_index=True)
    def __str__(self):
        return self.title


# Create your models here.
