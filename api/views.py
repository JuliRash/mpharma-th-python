from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse

from rest_framework import viewsets
import pandas as pd
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from api import serializers
from api.models import Diagnosis
from api.serializers import DiagnosisSerializer, UploadSerializer
from api.tasks import import_data_to_db


def index(request):
    return render(request, 'index.html')


def api_root(request):
    return JsonResponse({'diagnosis': reverse('diagnosis')})


class DiagnosisViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows diagnosis to be viewed or edited.
    """
    queryset = Diagnosis.objects.all().order_by('-added_at')
    serializer_class = DiagnosisSerializer


class UploadViewSet(viewsets.ViewSet):
    """
    API endpoint that allows csv file to be uploaded and imported
    """
    serializer_class = UploadSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def create(self, request):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            file_uploaded = request.FILES.get('file_uploaded')
            if(file_uploaded.content_type != 'text/csv'):
                return Response({'status': 'error', 'data': ' File type must be of csv'}, status=status.HTTP_400_BAD_REQUEST)
            email = request.POST.get('email')

            reader = pd.read_csv(file_uploaded, header=None)
            import_data_to_db.delay(reader.to_json(), email)

            message = "data import processing a confirmation email would be sent to " + \
                email + " after completion"
            return Response({'status': 'success', 'message': message}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
