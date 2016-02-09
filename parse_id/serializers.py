from rest_framework import serializers
from .models import id_desc

class base_serializer(serializers.ModelSerializer):
    class Meta:
        model = id_desc
        fields = ('db','db_id','id_desc')
