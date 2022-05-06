from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view, action
from .serializer import *
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from datetime import datetime
# Create your views here.

@api_view(['GET'])
def Get_Slider(request):
    a = Slider.objects.all().order_by('-id')[:3]
    ser = SliderSerializer(a, many=True)

    return Response(ser.data)

@api_view(['GET'])
def Get_Info(request):
    a = Info.objects.last()
    ser = InfoSerializer(a)

    return Response(ser.data)


@api_view(['GET'])
def Get_Welcome(request):
    a = welcome_text.objects.last()
    ser = WelcomeSerializer(a)

    return Response(ser.data)

@api_view(['GET'])
def Get_Service(request):
    a = Service.objects.all().order_by('-id')[:3]
    ser = ServiceSerializer(a, many=True)

    return Response(ser.data)

@api_view(['GET'])
def Get_Hots(request):
    a = Product.objects.filter(category__name='Pizza').order_by('-id')[:6]
    ser = ProductSerializer(a, many=True)

    return Response(ser.data)

@api_view(['GET'])
def Get_Pricing(request):
    a = Product.objects.filter(category__name='Pizza', price__gte=19, price__lte=50).order_by('-id')[:8]
    ser = ProductSerializer(a, many=True)

    return Response(ser.data)


@api_view(['GET'])
def Get_Achievement(request):
    a = Achievement.objects.all().order_by('-id')[:4]
    ser = AchievementSerializer(a, many=True)

    return Response(ser.data)

@api_view(['GET'])
def Filter_Category(request):
    types = request.GET['type']
    a = Product.objects.filter(category__name=types)
    ser = ProductSerializer(a, many=True)

    return Response(ser.data)

@api_view(['GET'])
def Get_Blog(request):
    a = Blog.objects.all()
    ser = BlogSerializer(a, many=True)

    return Response(ser.data)

@api_view(['GET'])
def Filter_Blog(request):
    types = request.GET['type']
    a = Blog.objects.filter(category__name=types)
    ser = BlogSerializer(a, many=True)

    return Response(ser.data)

@api_view(['POST'])
def Create_Contact(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    message = request.POST.get('message')
    a = Contact.objects.create(first_name=first_name, last_name=last_name, message=message)
    ser = ContactSerializer(a)

    return Response(ser.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Add_Cart(request):
    product_id = request.POST.get('product')
    user = request.user
    product = Product.objects.get(id=product_id)
    a = Cart.objects.create(product=product, user=user)
    ser = CartSerializer(a)

    return Response(ser.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Del_Cart(request):
    cart_id = request.POST.get('id')
    user = request.user
    a = Cart.objects.get(id=cart_id, user=user)
    a.delete()  

    return Response({'status': "Muvaffaqiyatli o'chirildi!"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Get_Cart(request):
    user = request.user
    Carts = Cart.objects.filter(user=user)
    ser = CartSerializer(Carts, many=True)

    return Response(ser.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Add_Order(request):
    n = []
    user = request.user
    Carts = Cart.objects.filter(user=user)
    for i in Carts:
        a = Order.objects.create(user=user, product=i.product, price=i.product.price, date=datetime.today())
        n.append(a)
        i.delete()
    ser =OrderSerializer(n, many=True)
    return Response(ser.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Get_Order(request):
    user = request.user
    a = Order.objects.filter(user=user)
    ser = OrderSerializer(a, many=True)

    return Response(ser.data)