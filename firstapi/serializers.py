from rest_framework import serializers

from firstapp.models import UserFiles


class FileInputSerializer(serializers.ModelSerializer):
    image = serializers.FileField()

    class Meta:
        model = UserFiles
        fields = ['image']
