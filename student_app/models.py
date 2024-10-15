from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    courses = models.ManyToManyField("Course", blank=True)

    class Meta:
        verbose_name_plural = 'Student'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()

    class Meta:
        unique_together = ("name", "year")

    def __str__(self):
        return f"{self.name} {self.year}"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField(validators=[MinValueValidator(0),
                                                    MaxValueValidator(100)])

    def __str__(self):
        return f"{self.student} {self.course} {self.grade}"
