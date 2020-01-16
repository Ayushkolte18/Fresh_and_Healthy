from .models import CartItem
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from django.http import Http404
from .serializers import CartSerializer
from Cart.models import Cart


class CartAPI(APIView):
    def get(self, request):
        user = Cart.objects.get(user=request.user)
        if user.is_exist():
            snnipets = CartItem.objects.all()
            serializer = CartSerializer(snnipets, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Update(APIView):
    def get_object(self, pk):
        try:
            return CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExist:
            raise Http404

    def get(self, request,pk):
        snnipets = CartItem.objects.get(pk=pk)
        serializer = CartSerializer(snnipets)
        breakpoint()
        return Response(serializer.data)

    def put(self, request, pk):
        snnipets = CartItem.objects.get(pk=pk)
        serializer = CartSerializer(snnipets, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        snnipets = CartItem.objects.get(pk=pk)
        snnipets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

