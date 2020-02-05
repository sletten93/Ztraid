from django.contrib.auth.models import AbstractUser
from django.db import models

"""

Django-modeller baserade på det första sambandsdiagrammet.

- Alla primärnycklar tillåts i nuläget skapas av Django och ser ut som nedandför:
    "id" serial NOT NULL PRIMARY KEY 
    stycket ovanför är skrivet i PostgreSQL syntax, aktuell syntax beror på vald databastyp i settings.py

- Kopplingstabeller är implementerade m.h.a models.ManyToManyField

"""



class Product(models.Model):

    name = models.CharField(max_length=20)
    cost = models.FloatField(max_length=10)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Devices(models.Model):

    name = models.CharField(max_length=20)
    OS = models.CharField(max_length=20)
    CPU = models.CharField(max_length=20)
    GPU = models.CharField(max_length=20)
    cam = models.CharField(max_length=20)
    mic = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True)

    # TODO - de flesta def __str__(self): är placeholder functions, gör dem användbara eller ta bort

    def __str__(self):
        return self.name


class ZtrUser(AbstractUser):

    #   name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    role = models.CharField(max_length=1)
    nickname = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    salt = models.CharField(max_length=25)
    password = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True)

    user_products = models.ManyToManyField(Product)
    user_devices = models.ManyToManyField(Devices)

    def __str__(self):
        return "{} {}".format(self.username, self.nickname)

    def get_role(self):
        return self.role


class UserPref(models.Model):

    # TODO on_delete=models.CASCADE <-- passande??
    user_ID = models.OneToOneField(ZtrUser, on_delete=models.CASCADE)
    net_speed = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_ID


class FAQ(models.Model):

    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=8000)
    example = models.CharField(max_length=8000)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class Paragraph(models.Model):

    text = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
