from rest_framework import serializers
# from django.contrib.auth.models import User

from baseApp.models import INCTicket, SRTicket


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = INCTicket
        fields = '__all__'


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = INCTicket
        fields = ('ticket', 'status', 'created', 'description')


class SRSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRTicket
        fields = ('tickets', 'status', 'created', 'description')

