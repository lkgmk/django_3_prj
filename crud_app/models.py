from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class NameDetails(models.Model):
    id = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}  {self.person_name}  {self.country_name}'


# One to one
def check_reg_no(value):
    if value and value > 0:
        return value
    raise ValidationError(f"{value} sholud be greater than 0.")


class Vehicle(models.Model):
    reg_no = models.IntegerField(validators=[check_reg_no])
    owner = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.reg_no}  {self.owner}'


class Car(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, primary_key=True)
    car_model = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.vehicle}  {self.car_model}'


# Many to one
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}  {self.artist}'


class Songs(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}  {self.album}'


# Many to Many
class Author(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.name}  {self.desc}'


class Book(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        author_names = ', '.join(author.name for author in self.authors.all())
        return f'{self.title}  {self.desc} written by {author_names}'
