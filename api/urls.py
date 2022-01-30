from distutils.command.upload import upload
from unicodedata import name
from django.urls import include, path
from rest_framework import routers

from . import views
from api.views import DiagnosisViewSet, UploadViewSet, api_root


router = routers.DefaultRouter()

diagnosis_list = DiagnosisViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)


diagnosis_detail = DiagnosisViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }
)

upload_view = UploadViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)

urlpatterns = [
    path('', api_root, name='apiroot'),
    path('diagnosis', diagnosis_list, name='diagnosis'),
    path('diagnosis/<str:pk>', diagnosis_detail, name='detail'),
    path('diagnosis/csv-upload', upload_view, name='upload_csv')
]
