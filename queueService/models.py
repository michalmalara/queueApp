from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey('auth.User', related_name='stations', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Station {self.name}"


class Case(models.Model):
    name = models.CharField(max_length=100, unique=True)
    stations = models.ManyToManyField(Station, related_name='cases')
    symbol = models.CharField(max_length=1, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Case {self.name}"
