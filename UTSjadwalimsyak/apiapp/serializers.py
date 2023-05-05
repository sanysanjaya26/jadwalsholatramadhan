from rest_framework import serializers
from . models import Jadwal_imsyak

class Jadwalserializers(serializers.ModelSerializer):
    class Meta:
        model = Jadwal_imsyak
        fields = '__all__'

