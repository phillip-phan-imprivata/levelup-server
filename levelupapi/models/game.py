from django.db.models.fields import CharField, IntegerField
from django.db import models
from django.db.models.fields.related import ForeignKey

class Game(models.Model):
  title = CharField(max_length=50)
  maker = CharField(max_length=50)
  gamer = ForeignKey("Gamer", on_delete=models.CASCADE)
  gametype = ForeignKey("GameType", on_delete=models.CASCADE)
  number_of_players = IntegerField()
  skill_level = IntegerField()
