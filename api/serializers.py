from api.models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Faculty

class FacSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = "__all__"

