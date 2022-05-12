from django.db import models

# Create your models here.


class Athlete(models.Model):

    year_choices = [(1, 'First Year'), (2, 'Second Year'), (3, 'Third Year'), (4, 'Fourth Year'), (5, 'Postgraduate')]

    name = models.CharField(max_length=100)
    year = models.IntegerField(choices=year_choices)
    batch = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Event(models.Model):

    name = models.CharField(max_length=50)
    first = models.ManyToManyField(Athlete, related_name='first')
    first_points = models.IntegerField()
    second = models.ManyToManyField(Athlete, related_name='second')
    second_points = models.IntegerField()
    third = models.ManyToManyField(Athlete, related_name='third')
    third_points = models.IntegerField()

    def __str__(self):
        return self.name
