from rest_framework import serializers

from firstapp.models import SystemUser, Client


class InsertUserSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        user_name = validated_data.get('user_name')
        name = validated_data.pop('name')
        obj: SystemUser = super(InsertUserSerializer, self).create(validated_data)
        obj1: Client = obj.user_client.create(name=name)
        obj1.save()
        return obj

    def update(self, instance, validated_data):
        user_name = validated_data.get('user_name')
        name = validated_data.pop('name')
        obj: SystemUser = super(InsertUserSerializer, self).update(instance=instance, validated_data=validated_data)
        obj1: Client = obj.user_client.update(name=name)
        return obj

    class Meta:
        model = SystemUser
        fields = ['user_name', 'name']


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemUser
        fields = ['id', 'user_name', 'name']
