from django.db import models
from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


    
class Sensor(models.Model):
    id =  models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        

    def __str__(self):
        return self.name   

class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    image = models.ImageField(blank=True)




