from django.db import models


class Eye(models.Model):
    char = models.CharField(max_length=1)

    def __str__(self):
        return self.char


class Nose(models.Model):
    char = models.CharField(max_length=1)

    def __str__(self):
        return self.char


class Mouth(models.Model):
    char = models.CharField(max_length=1)

    def __str__(self):
        return self.char
