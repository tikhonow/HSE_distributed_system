# processor/serializers.py

from rest_framework import serializers

class NumberSerializer(serializers.Serializer):
    number = serializers.IntegerField(
        min_value=0,
        error_messages={
            'min_value': 'Number must be a natural number (>= 0).',
            'invalid': 'A valid integer is required.'
        }
    )
