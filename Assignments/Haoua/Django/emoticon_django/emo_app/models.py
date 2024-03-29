from django.db import models

class FacePart(models.Model):
    char = models.CharField(max_length=1)
    def __str__(self):
           return self.char

    class Meta:
        abstract = True # Tell django that this is an abstract class

class Eye(FacePart):
    pass

class Nose(FacePart):
    pass

class Mouth(FacePart):
    pass