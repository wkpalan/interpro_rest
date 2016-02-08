from django.db import models

# Create your models here.
class id_desc(models.Model):
    db = models.CharField(max_length=100)
    db_id = models.CharField(max_length=50)
    id_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.db_id
