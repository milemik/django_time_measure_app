from timers.models import Timer, PauseTimes
from rest_framework import serializers
from django.utils import timezone


class TimerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timer
        fields = ['name']


class DetailTimerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timer
        fields = ['name', 'start_time', 'finish_time', 'time', 'active_time']
        read_only_fields = ['name', 'start_time', 'finish_time', 'time',
                            'active_time']

    def update(self, instance, validated_data):
        print(instance.finish_time)
        if instance.finish_time is None:
            instance.finish_time = timezone.now()
            instance.save()
        else:
            raise serializers.ValidationError('This Timer is finished!')
        return instance


class PauseSerializer(serializers.ModelSerializer):

    class Meta:
        model = PauseTimes
        fields = ['id', 'timer', 'start', 'stop', 'pause_time']
        read_only_fields = ['id', 'start', 'stop', 'pause_time']

    def create(self, validated_data):
        timer = Timer.objects.get(id=validated_data.get('timer').id)
        if timer.finish_time is not None:
            raise serializers.ValidationError(
                'You can\'t pause what is finished'
                )
        if PauseTimes.objects.filter(timer=validated_data.get('timer').id,
                                     stop=None).exists():
            raise serializers.ValidationError("You have pause runing")
        else:
            pt = PauseTimes.objects.create(**validated_data)
            return pt

    def update(self, instance, validated_data):
        if instance.stop is None:
            instance.stop = timezone.now()
            instance.save()
        else:
            raise serializers.ValidationError('This pause is over!')
        return instance
