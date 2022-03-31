from rest_framework import serializers
from .models import Control_words

class RaspSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control_words
        fields = ('user_id','name','title','text')