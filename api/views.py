import json

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import CandidateSerializer
from .models import Candidate
from django.db.models import Q

class CandidateList(APIView):
    """
    Candidate List view
    """

    def get(self, request: Request) -> Response:
        """
        Get list of candidates
        """
        query_params = request.query_params
        
        query = Q()

        if "name" in query_params:
            words = query_params["name"].split()
            for word in words:
                query |= Q(name__icontains=word)
        
        candidates = Candidate.objects.filter(query)
        
        return Response(CandidateSerializer(candidates, many=True).data, status=status.HTTP_200_OK) 


    def post(self, request: Request) -> Response:
        """
        Create the candidate
        """

        serializer = CandidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CandidateDetail(APIView):
    """
    Candidate Detail View
    """

    def put(self, request: Request, id: str) -> Response:
        """
        Update the candidate
        """

        try:
            candidate = Candidate.objects.get(id=id)
        except:
            return Response("invalid id or candidate not exist", status=status.HTTP_400_BAD_REQUEST)

        serializer = CandidateSerializer(candidate, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request:Request, id: str) -> Response:
        """
        delete the candidate
        """

        try:
            candidate = Candidate.objects.get(id=id)
        except:
            return Response("invalid id or candidate not exist", status=status.HTTP_400_BAD_REQUEST)
        
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

