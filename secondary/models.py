from django.db import models


# Create your models here.

class Science(models.Model):
    subject = models.CharField(max_length=50, null=False)
    reading = models.CharField(max_length=50, null=False)
    marks = models.CharField(max_length=50, null=False)
    virtue = models.CharField(max_length=50, null=False)
    interested = models.CharField(max_length=50, null=False)

    def __str__(self):
        return "Science"


class Arts(models.Model):
    subject = models.CharField(max_length=50, null=False)
    reading = models.CharField(max_length=50, null=False)
    marks = models.CharField(max_length=50, null=False)
    virtue = models.CharField(max_length=50, null=False)
    interested = models.CharField(max_length=50, null=False)

    def __str__(self):
        return "Arts"


class Commerce(models.Model):
    subject = models.CharField(max_length=50, null=False)
    reading = models.CharField(max_length=50, null=False)
    marks = models.CharField(max_length=50, null=False)
    virtue = models.CharField(max_length=50, null=False)
    interested = models.CharField(max_length=50, null=False)

    def __str__(self):
        return "Commerce"
