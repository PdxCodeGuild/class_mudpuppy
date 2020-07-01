from django.db import models

class FacePart(models.Model):
    char = models.CharField(max_length=1)
    def __str__(self):
        return self.char

    class Meta:
        abstract = True

class Eye(FacePart):
    pass
class Nose(FacePart):
    pass
class Mouth(FacePart):
    pass

# class Eye(models.Model):
#     char = models.CharField(max_length=1)

#     def __str__(self):
#         return self.char

# class Nose(models.Model):
#     char = models.CharField(max_length=1)

#     def __str__(self):
#         return self.char

# class Mouth(models.Model):
#     char = models.CharField(max_length=1)

#     def __str__(self):
#         return self.char

# Create your models here.
