from django.db import models
from django.shortcuts import reverse
# Create your models here.


# todo: DO SAVE THE FIRST OBJECT AS : template1.html   -from the admin panel
class CVTemplate(models.Model):
     name = models.CharField(max_length=100)
     template = models.CharField(max_length=200)

     def get_absolute_url(self):
        return reverse('cv-detail', args=[str(self.id)])
     def __str__(self):
          return self.name