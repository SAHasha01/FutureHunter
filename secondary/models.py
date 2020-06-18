from django.db import models


# Create your models here.

class secondary(models.Model):
    question = models.CharField(max_length=200)
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    answer = models.BooleanField(choices=BOOL_CHOICES)

    def __str__(self):
        return str(self.id)


