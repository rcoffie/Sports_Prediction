from rest_framework import serializers
from dashboard.models import Data


class WriteDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['id','name','age','height','predictions','date']

        extra_kwargs = {
        'predictions': {'write_only': True},
        }


class ReadDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['id','name','age','height','predictions','date']

        read_only_fields = fields
