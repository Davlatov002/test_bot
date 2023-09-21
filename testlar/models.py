from django.db import models

class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    savol = models.CharField(max_length=1000)
    javoblar = models.CharField(max_length=500)
