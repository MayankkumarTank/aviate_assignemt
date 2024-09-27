"""
Candidate serializers
"""

from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    """
    Create candidate serializer
    """

    class Meta:
        model = Candidate
        fields = "__all__"