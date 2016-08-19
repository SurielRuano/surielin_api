from rest_framework import generics
from ..models import Carro
from .serializers import CarroSerializer



class CarroListView(generics.ListAPIView):

	queryset = Carro.objects.all()
	serializer_class =  CarroSerializer

class CarroListView(generics.RetrieveAPIView):
	queryset = Carro.objects.all()
	serializer_class = CarroSerializer

