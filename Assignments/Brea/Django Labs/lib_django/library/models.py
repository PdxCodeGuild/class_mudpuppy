from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=128)
    publish_date = models.DateField()
    author = models.ForeignKey('Author', on_delete=models.PROTECT)

class Author(models.Model):
    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    middle1 = models.CharField(max_length=16, blank=True, null=True)
    middle2 = models.CharField(max_length=16, blank=True, null=True)

    def name_formatted(self):
        output = f"{self.last_name}, {self.first_name}"
        if self.middle1:
            output += f" {self.middle1}"
            if self.middle2:
                output += f" {self.middle2}"
        return output

class Checkout(models.Model):
    book = models.ForeignKey('Book', on_delete=models.PROTECT)
    user = models.CharField(max_length=32)
    checkout = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

