from rest_framework import serializers
from django.core.validators import RegexValidator


phone_number_regex = RegexValidator(  
                                    regex=r'^09(1[0-9]|3[0-9])[0-9]{7}$', 
                                    message="mobile phone number must be in this format '09123456789' and exactly 11 digits."
                                )

class SendTextSerializer(serializers.Serializer):
    phone_number = serializers.CharField(validators=[phone_number_regex])
    email = serializers.EmailField()
    text = serializers.CharField()
