from django.shortcuts import render
from . models import Jadwal_imsyak 
from . serializers import Jadwalserializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def readJadwal_imsyak(request): 
    ramadhan = Jadwal_imsyak.objects.all()
    serializers = Jadwalserializers(ramadhan, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def readJadwal_imsyakiyah(request, id): 
    ramadhan = Jadwal_imsyak.objects.get(pk=id)
    serializers = Jadwalserializers(ramadhan, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def createjadwal(request):
    serializer = Jadwalserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updatejadwal(request, id):
    jadwalImsyak = Jadwal_imsyak.objects.get(pk=id)
    serializer = Jadwalserializers(instance=jadwalImsyak, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletejadwal(request, id):
    jadwalImsyak = Jadwal_imsyak.objects.get(pk=id)
    jadwalImsyak.delete()

    return Response('data sudah di hilangkan', status=204)
