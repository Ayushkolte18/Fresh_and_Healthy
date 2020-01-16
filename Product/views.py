from django.shortcuts import render
from .models import Product, Category
from .serializers import Prdouct_serializer, Category_serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.
# class Product_API(APIView):
#
#     def get(self, request):
#         snnipet = Product.objects.all()
#         serializer = Prdouct_serializer(snnipet, many=True)
#         return Response(serializer.data)
#
#
# class By_Serach(APIView):
#
#     def get(self, request, name):
#         snippets = Product.objects.filter(title=name)
#         if len(snippets) >= 1:
#             serializer = Prdouct_serializer(snippets, many=True)
#             return Response(serializer.data)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#
# class Categories_API(APIView):
#
#     def get(self, request, pk):
#         snippets = Category.objects.get(pk=pk)
#         snippets1 = snippets.get_children()
#         if len(snippets1) >= 1:
#             serializer = Category_serializer(snippets1, many=True)
#             return Response(serializer.data)
#         else:
#             return Response(status=status.HTTP_204_NO_CONTENT)


class Standard(APIView):
    def get(self, request):
        snippets = Product.objects.filter(status="Standard")
        serializer = Prdouct_serializer(snippets, many=True)
        return Response(serializer.data)

    class By_Search(APIView):
        def get(self, request, name):
            snippets = Product.objects.filter(title=name, status="Standard", avail="Always")
            if len(snippets) >= 1:
                serializer = Prdouct_serializer(snippets, many=True)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

    # class Categories_API(APIView):
    #     def get(self, request):
    #         snippets = Category.objects.get(pk=2)
    #         snippets1 = snippets.get_children()
    #         if len(snippets1) >= 1:
    #             serializer = Category_serializer(snippets1, many=True)
    #             return Response(serializer.data)
    #         else:
    #             return Response(status=status.HTTP_204_NO_CONTENT)


class Immediate(APIView):
    def get(self, request):

        snippets = Product.objects.exclude(status="Advanced")
        serializer = Prdouct_serializer(snippets, many=True)
        return Response(serializer.data)


    class By_Serach(APIView):

     def get(self, request, name):
        snippets = Product.objects.filter(title=name, status="Immediate")
        if len(snippets) >= 1:
            serializer = Prdouct_serializer(snippets, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class Advanced(APIView):

    def get(self, request):
        snippets = Product.objects.all()
        serializer = Prdouct_serializer(snippets, many=True)
        return Response(serializer.data)

    class By_Serach(APIView):

        def get(self, request, name):
            snippets = Product.objects.filter(title=name, status="Advanced")
            if len(snippets) >= 1:
                serializer = Prdouct_serializer(snippets, many=True)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
