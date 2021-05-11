from django.db import models

class Event(models.Model):
  description = models.CharField(max_length=100)
  organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
  game = models.ForeignKey("Game", on_delete=models.CASCADE)
  date = models.CharField(max_length=50)
  time = models.CharField(max_length=50)
  attendees = models.ManyToManyField("Gamer", through="gamerevent", related_name="attending")

  @property
  def joined(self):
      return self.__joined

  @joined.setter
  def joined(self, value):
      self.__joined = value