from django.db import models


class Timer(models.Model):

    name = models.CharField(max_length=50)
    start_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField(null=True)


class PauseTimes(models.Model):

    timer = models.ForeignKey(Timer, on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now_add=True)
    stop = models.DateTimeField(null=True)
