import re
from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'email', 'text', 'created_date', 'update_date']

    def validate_email(self, email):
        norm_email = email.lower()
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if not re.search(regex, norm_email):
            raise serializers.ValidationError('Enter a valid Email')
        return norm_email

    def validate_text(self, text):
        regex = '^(?!\s*$).{,99}$'
        if not re.search(regex, text):
            raise serializers.ValidationError(
                'The message must not be empty string and must not be longer than 100 characters')
        return text
