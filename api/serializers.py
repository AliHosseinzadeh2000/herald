from rest_framework import serializers


class SendTextSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    email = serializers.CharField()
    text = serializers.CharField()
