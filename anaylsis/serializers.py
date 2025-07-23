from rest_framework import serializers
from .models import App

class NoteSerializer(serializers.ModelSerializer):
    class Mets:
        model = App
        fields = '__all__'
