from rest_framework import serializers
from .models import NameDetails


class NameDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameDetails
        fields = '__all__'
