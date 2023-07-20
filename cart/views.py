from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart
from datetime import datetime


from .serializers import AddCartSerializer,GetCartSerializer

# Create your views here.


class AddCart(APIView):
    def post(self, request, format=None):
        serializer = AddCartSerializer(data=request.data)
        print(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 200})
        else :
            return Response({'msg': 404})
        

class CartView(APIView):
    def get(self, request, pk):
        cart = Cart.objects.filter(user=pk)
        
        serializer = AddCartSerializer(cart, many=True)
        
        total =0

        
        return Response(serializer.data)
    
class GetCartView(APIView):
    def get(self, request, pk):
        cart = Cart.objects.filter(user=pk)
        
        total =0
      
        
        serializer = GetCartSerializer(cart, many=True)
        
        return Response({'data':serializer.data, 'total':total})



  
class RemoveCart(APIView):
    def delete(self, request, pk):
        try:
            cart = Cart.objects.get(id=pk)
            cart.delete()
            return Response({'msg': 200})
        except:
            cart.DoesNotExist
            return Response({'msg': 500})
        
 
        
        
        
   
        
        
        
