from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Jersey
from .serializers import JerseySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.db.models import Q
class JerseyList(APIView):#endpoint camisetas#
    def get(self, request): 
        q_filter = request.query_params.get("q_filter")
        filters = Q()
        if q_filter:
            filters &= Q(category=q_filter)
        jerseys = Jersey.objects.filter(filters)
        serializer = JerseySerializer(jerseys, many=True)
        return Response({
            "success": True,
            "status": status.HTTP_200_OK,
            "data": serializer.data
        })

    def post(self, request):
        serializer = JerseySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JerseyListCreateView(ListCreateAPIView):
    queryset = Jersey.objects.all()
    serializer_class = JerseySerializer

class JerseyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Jersey.objects.all()
    serializer_class = JerseySerializer
