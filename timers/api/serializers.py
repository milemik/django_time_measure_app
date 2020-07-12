from timers.models import Timer, PauseTimes
from rest_framework import serializers
from datetime import datetime


class TimerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timer
        fields = ['name']


class DetailTimerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timer
        fields = ['name', 'start_time', 'finish_time']
        read_only_fields = ['name', 'start_time', 'finish_time']

    def update(self, instance, validated_data):
        print(instance.finish_time)
        if instance.finish_time is None:
            instance.finish_time = datetime.now()
            instance.save()
        else:
            raise serializers.ValidationError('This Timer is finished!')
        return instance


class PauseSerializer(serializers.ModelSerializer):

    class Meta:
        model = PauseTimes
        fields = ['timer']

    def update(self, instance, validated_data):
        if instance.stop is None:
            instance.stop = datetime.now()
            instance.save()
        else:
            raise serializers.ValidationError('This pause is over!')
        return instance
