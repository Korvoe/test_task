from rest_framework import serializers
from .models import VPS

class vpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPS
        fields = "__all__"



class vpsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPS
        fields = "__all__"
        read_only_fields = ('uid', 'hdd', 'cpu', 'ram')

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
