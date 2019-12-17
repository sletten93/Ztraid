from django.db import models

class Ztr_User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    role = models.CharField(max_length=1)
    nickname = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    salt = models.CharField(max_length=25)
    password = models.CharField(max_length=20)

    def __str__(self):
        return "{} {}".format(self.name, self.nickname)

class User_Pref(models.Model):
    net_speed = models.IntegerField(max_length=10)
    #TO-DO, fixa en-till-en relation
    #on_delete=models.CASCADE <-- passande?
    user_id = models.ForeignKey(Ztr_User)