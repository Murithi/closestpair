
from rest_framework import serializers
from msfapp.models import ClosePairs

class ClosePairsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClosePairs
        fields = ["submitted_points", "closest_pair", "timestamp"]