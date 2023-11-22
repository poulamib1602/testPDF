# pdf_app/serializers.py
from rest_framework import serializers

class UploadFileSerializer(serializers.Serializer):
    pdf_file = serializers.FileField()
