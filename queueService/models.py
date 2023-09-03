from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', related_name='stations', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Station {self.name}"


class Case(models.Model):
    name = models.CharField(max_length=100)
    stations = models.ManyToManyField(Station, related_name='cases')

    def __str__(self):
        return f"Case {self.name}"
