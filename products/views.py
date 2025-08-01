from django.shortcuts import render
from rest_framework.generics import GenericAPIView , mixins
from .models import Chocolate
from .serializer import ChocolateSerializer
# Create your views here.

class ListCreateApi(GenericAPIView , mixins.ListModelMixin , mixins.CreateModelMixin):
    queryset = Chocolate.objects.all()
    serializer_class = ChocolateSerializer

    def get(self , request , *args , **kwargs):
        return self.list(request , *args , **kwargs)

    def post(self , request , *args , **kwargs):
        return self.create(request , *args , **kwargs)

class DetailView(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
        queryset = Chocolate.objects.all()
        serializer_class = ChocolateSerializer

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)

        def put(self, request, *args , **kwargs):
            return self.update(request , *args , **kwargs)

        def patch(self, request, *args , **kwargs):
            return self.partial_update(request , *args , **kwargs)

        def delete(self, request, *args , **kwargs):
            return self.destroy(request, *args , **kwargs)