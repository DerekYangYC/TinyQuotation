from django.db import models


class User(models.Model):
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    ali_id = models.CharField(max_length=250)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    created_date = models.DateTimeField('created date')
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.account + ":" + self.aliId + ":" + self.name


class Order(models.Model):
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.name