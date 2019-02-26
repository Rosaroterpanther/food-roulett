from django.db import models

# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    food_description = models.CharField(max_length=200)

    def __str__(self):
        return self.food_name
