from rest_framework import serializers


# class AdSerializer(serializers.Serializer):
# name = serializers.CharField(max_length=100)
# author_id
# price


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
