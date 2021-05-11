from django.db import models

class Token(models.Model):
  gamer = models.OneToOneField("Gamer", on_delete=models.CASCADE)
  created = models.CharField(max_length=50)