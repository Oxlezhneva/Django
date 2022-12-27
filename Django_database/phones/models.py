from django.db import models

class Phone(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    image = models.TextField()
    release_date= models.TextField()
    lte_exists= models.TextField()
    slug = models.SlugField(max_length=255)


