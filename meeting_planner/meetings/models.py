from django.db import models

# Create your models here.


# criando titulos das tabelas
class Meeting(models.Model):
    title = models.CharField(max_lenght=200)
    date = models.DateField()


