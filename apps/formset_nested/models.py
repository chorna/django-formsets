from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_cant_cellphone(self):
        return self.cellphone_set.all().count()


class CellPhone(models.Model):
    contact = models.ForeignKey(Contact)
    number = models.CharField(max_length=20)


class Email(models.Model):
    contact = models.ForeignKey(Contact)
    mail = models.EmailField()