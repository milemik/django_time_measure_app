from django.urls import path
from .views import TimerView, PauseTimerView, EndTimerView, StopPauseTimerView


urlpatterns = [
    path('', TimerView.as_view(), name='timers'),
    path('<int:pk>/', EndTimerView.as_view(), name='end-timer'),
    path('pause/', PauseTimerView.as_view(), name='pause'),
    path('pause/<int:pk>/', StopPauseTimerView.as_view(), name='pause-stop'),
]
