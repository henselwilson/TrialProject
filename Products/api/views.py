from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from .serializers import OrderSerial
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def make_order(request,*args,**kwargs):
    user1=request.user

    serializer = OrderSerial(user=user1)
    print(serializer.is_valid())
    data={'abc':'cde'}
    return Response(data=data)
