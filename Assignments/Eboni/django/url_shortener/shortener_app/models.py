from django.db import models



# Create your models here.

class Code(models.Model):
    first_code = models.CharField(max_length=100)
    second_code = models.CharField(max_length=100)
    

    def __str__(self):
        return self.first_code
"""
for i in Code.objects.all():
...     if i.first_code[0] == "w":
...             i.delete()
"""
