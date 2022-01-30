
from rest_framework import serializers

from api.models import Diagnosis


class DiagnosisSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(max_length=255)
    category_code = serializers.CharField(max_length=255)
    full_code = serializers.CharField(max_length=255)
    abbreviated_description = serializers.CharField(max_length=255)
    diagnosis_code = serializers.CharField(max_length=255)
    full_description = serializers.CharField()

    class Meta:
        model = Diagnosis
        fields = ('__all__')


class UploadSerializer(serializers.Serializer):
    file_uploaded = serializers.FileField()
    email = serializers.EmailField()

    class Meta:
        field = ['file_uploaded', 'email']
