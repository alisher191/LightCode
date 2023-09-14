from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .serializers import PersonSerializer
from .models import Person


class PersonAPIView(ListCreateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

