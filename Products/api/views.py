from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from .serializers import OrderSerial
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from Products.models import Orders,Phone

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def make_order(request,*args,**kwargs):
    user1=request.user
    phone1 = request.data['phone']
    request_quantity = request.data['quantity']
    print(user1, phone1, request_quantity)
    Phone_inst = Phone.objects.filter(title=phone1).first()
    q_avail = Phone_inst.quantity_available
    id1=Phone_inst.id
    print(id1)
    print(q_avail)
    if q_avail-request_quantity>=0:
        Orders.objects.create(user=user1, product_id=Phone_inst, quantity=request_quantity)
        print("******")
        phoneinst2=Phone.objects.get(id=id1)
        print(phoneinst2.quantity_available)
        #Phone_q_update = Phone.objects.filter(title=phone1).first()
        phoneinst2.quantity_available = q_avail-request_quantity
        print("########")
        print(Phone_inst.quantity_available)
        print(Phone_inst)
        phoneinst2.save()
        return Response(phoneinst2)
    data = {'abc': 'cde'}
    return Response(data)