from django.db import models

class Sign(models.Model):
    sign = models.CharField(max_length= 20)
    lower_date = models.DateTimeField()
    upper_date = models.DateTimeField()

    def check_date(self, in_date):
        month = in_date.month
        day = in_date.day
        if month == 1 and day <=19:
            in_date = in_date.replace(year=2021)
            print(2021) 
        else:     
            in_date = in_date.replace(year=2020)
            print(2020)
        return in_date >= self.lower_date and in_date <= self.upper_date

    def __str__(self):
        return self.sign
    

class Birthday(models.Model):
    date = models.DateField(null=True, blank=True)
    sign = models.ForeignKey(Sign, null=True, on_delete=models.PROTECT)
    def __str__(self):
        return f"{str(self.date)} {self.sign}"

    


# Create your models here.
