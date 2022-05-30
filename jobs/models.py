from django.db import models


class Job(models.Model):
    position = models.CharField(max_length=200, unique=True)
    company = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    salary = models.CharField(max_length=200, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.position} {self.company} {self.address}"
