from rest_framework import serializers


class DashboardKPISerializer(serializers.Serializer):
    agents = serializers.IntegerField()
    documents = serializers.IntegerField()
    evenements = serializers.IntegerField()
    conges = serializers.IntegerField()