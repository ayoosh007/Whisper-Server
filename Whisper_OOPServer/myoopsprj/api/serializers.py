from rest_framework import serializers

class AudioSerializer(serializers.Serializer):
    file = serializers.FileField()