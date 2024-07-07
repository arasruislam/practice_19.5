from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    instrument_type = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.first_name