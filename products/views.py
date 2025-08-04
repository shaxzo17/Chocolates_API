from django.shortcuts import render
from rest_framework.generics import GenericAPIView , mixins
from .models import Chocolate
from .serializer import ChocolateSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
#
# class ListCreateApi(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Chocolate.objects.all()
#     serializer_class = ChocolateSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = {
#         'price': ['lt', 'gt'],
#         'type': ['exact'],
#         'country': ['exact'],
#     }
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class DetailView(GenericAPIView,
#                  mixins.RetrieveModelMixin,
#                  mixins.UpdateModelMixin,
#                  mixins.DestroyModelMixin):
#     queryset = Chocolate.objects.all()
#     serializer_class = ChocolateSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)




class ChocolateListAPIView(APIView):
    def get(self, request):
        chocolates = Chocolate.objects.all()

        price_lt = request.GET.get('price__lt')
        price_gt = request.GET.get('price__gt')
        type = request.GET.get('type')
        country = request.GET.get('country')

        if price_lt:
            chocolates = chocolates.filter(price__lt=price_lt)
        if price_gt:
            chocolates = chocolates.filter(price__gt=price_gt)
        if type:
            chocolates = chocolates.filter(type__iexact=type)
        if country:
            chocolates = chocolates.filter(country__iexact=country)

        serializer = ChocolateSerializer(chocolates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChocoDetailAPIView(APIView):
    def post(self, request):
        serializer = ChocolateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            chocolate = Chocolate.objects.get(pk=pk)
        except Chocolate.DoesNotExist:
            return Response({"detail": "Chocolate not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ChocolateSerializer(chocolate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            chocolate = Chocolate.objects.get(pk=pk)
        except Chocolate.DoesNotExist:
            return Response({"detail": "Chocolate not found."}, status=status.HTTP_404_NOT_FOUND)

        chocolate.delete()
        return Response({"detail": "Chocolate delete."}, status=status.HTTP_204_NO_CONTENT)
