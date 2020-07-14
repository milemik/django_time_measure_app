from rest_framework import mixins, generics
from .serializers import (TimerSerializer,
                          PauseSerializer,
                          DetailTimerSerializer)
from timers.models import Timer, PauseTimes


class TimerView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = Timer.objects.all()
    serializer_class = TimerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EndTimerView(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   generics.GenericAPIView):

    queryset = Timer.objects.all()
    serializer_class = DetailTimerSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PauseTimerView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):

    queryset = PauseTimes.objects.all()
    serializer_class = PauseSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StopPauseTimerView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         generics.GenericAPIView):

    queryset = PauseTimes.objects.all()
    serializer_class = PauseSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)
