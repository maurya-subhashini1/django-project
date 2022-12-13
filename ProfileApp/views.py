from django.shortcuts import render
from rest_framework.response import Response
from ProfileApp.models import Profile
from rest_framework.decorators import api_view
from rest_framework import status
from bson import ObjectId

from .serializers  import ProfileSerializer
# from bson import ObjectId

# Create your views here.

@api_view(['GET'])
def index(request):
    try :
        profiles=Profile.objects.all()
        serialProfiles=ProfileSerializer(profiles ,many=True)
        return Response(serialProfiles.data)
    except:
          return Response({
            'status':404,
            'message':'data not found',
        })

    

 
@api_view(['GET'])
def profileView(request ,id):
    try:
        profile=Profile.objects.get(_id=ObjectId(id))
        serialProfile=ProfileSerializer(profile ,many=False)
        return Response(serialProfile.data)
    except:
          return Response({
            'status':404,
            'message':'data not found',
        })




@api_view(['POST'])
def addprofile(request):
    try:
        serialdata=ProfileSerializer(data=request.data)
        if serialdata.is_valid():
            serialdata.save()
        return Response(serialdata.data)
    except:
          return Response({
            'status':404,
            'message':'email already exit',
        })

    


@api_view(['POST'])
def updateProfile(request ,id):
    try :
        profile=Profile.objects.get(_id=ObjectId(id))
        serialprofile=ProfileSerializer(instance=profile ,data=request.data)
        if serialprofile.is_valid():
            serialprofile.save()
        return Response(serialprofile.data)
    except:
          return Response({
            'status':404,
            'message':'data not found',
        })





@api_view(['DELETE'])
def deleteProfile(request,id):
    try :
        profile=Profile.objects.get(_id=ObjectId(id))
        profile.delete()
        
        return Response("deleted successfully")

    except:
          return Response({
            'status':404,
            'message':'data not found',
        })
    
