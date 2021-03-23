from django.shortcuts import render
from rest_framework import viewsets
from .models import LanguageSalesforce
from .serializers import LanguageSerializer

class LanguageView(viewsets.ModelViewSet):
    queryset = LanguageSalesforce.objects.all()
    serializer_class = LanguageSerializer