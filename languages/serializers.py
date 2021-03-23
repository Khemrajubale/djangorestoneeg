from rest_framework import serializers
from .models import Language, LanguageSalesforce

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LanguageSalesforce
        fields = ('name',)