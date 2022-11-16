from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import User
from .serializer import UserCreateSerializer
from excel_response import ExcelResponse


@api_view(['GET'])
def getDataXLSX(request):
    items = User.objects.all()
    serializer = UserCreateSerializer(items, many=True)
    return ExcelResponse(serializer.data)


@api_view(['GET'])
def getData(request):
    items = User.objects.all()
    serializer = UserCreateSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UserCreateSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)