from django.db import models


# Create your models here.
class NameDetails(models.Model):
    id = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)

    # def __str__(self):
    #     return self.person_name
