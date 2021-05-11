from django.db import models

class Gamerevent(models.Model):
  event = models.OneToOneField("Event", on_delete=models.CASCADE)
  gamer = models.OneToOneField("Gamer", on_delete=models.CASCADE)