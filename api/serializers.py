from rest_framework import serializers
from .models import Store
from datetime import datetime 

class StoreDataViewSerializer(serializers.Serializer):
    key = serializers.CharField(max_length=256)
    value = serializers.CharField(max_length=256)
    posting_date = serializers.DateTimeField()
    def create(self, validated_data):
        """
        Create and return a new `Store` instance, given the validated data.
        """
        return Store.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.key = validated_data.get('key', instance.key)
        instance.value = validated_data.get('value', instance.value)
        instance.posting_date = validated_data.get('posting_date', instance.posting_date)
        instance.save()
        return instance

