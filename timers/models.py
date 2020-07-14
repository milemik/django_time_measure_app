from django.db import models
from django.utils import timezone


class Timer(models.Model):

    name = models.CharField(max_length=50)
    start_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField(null=True)

    @property
    def time(self):
        if self.finish_time is not None:
            return self.finish_time - self.start_time
        else:
            return timezone.now() - self.start_time

    @property
    def active_time(self):
        times = PauseTimes.objects.filter(timer=self.id)
        if len(times) > 0 and self.finish_time is None:
            sum_times = sum([t.pause_time for t in times])
            return (timezone.now() - self.start_time).seconds - sum_times
        elif len(times) > 0 and self.finish_time is not None:
            dif_time = self.finish_time - self.start_time
            sum_times = sum([t.pause_time for t in times])
            print("Times: {} and {}".format(self.finish_time, self.start_time))
            print("Finish minus start: {} = {}".format(dif_time,
                                                       dif_time.seconds))
            print(f"Sum pause times: {sum_times}")
            return (self.finish_time - self.start_time).seconds - sum_times
        elif self.finish_time is not None:
            return (self.finish_time - self.start_time).seconds
        else:
            return (timezone.now() - self.start_time).seconds


class PauseTimes(models.Model):

    timer = models.ForeignKey(Timer, on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now_add=True)
    stop = models.DateTimeField(null=True)

    @property
    def pause_time(self):
        if self.stop is None:
            return (timezone.now() - self.start).seconds
        else:
            return (self.stop - self.start).seconds
