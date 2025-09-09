from django.db import models

# Create your models here.
class Cars(models.Model):
    name = models.CharField("Марка", max_length=100)
    preview = models.ImageField("Превью",upload_to='cars/')
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
