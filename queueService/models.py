from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey("auth.User", related_name="stations", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Station {self.name}"


class Case(models.Model):
    name = models.CharField(max_length=100, unique=True)
    stations = models.ManyToManyField(Station, related_name="cases")
    symbol = models.CharField(max_length=1, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Case {self.name}"


class Queue(models.Model):
    case = models.ForeignKey(Case, related_name="queues", on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_started = models.DateTimeField(blank=True, null=True)
    datetime_completed = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    station = models.ForeignKey(Station, related_name="queues", on_delete=models.CASCADE, blank=True, null=True,
                                default=None)
    number = models.IntegerField(blank=True, null=True)
