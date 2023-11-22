# pdf_app/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('extract_pdf/', ExtractPDFView.as_view(), name='extract_pdf'),
     path('get_demo_data/', GetDemoDataView.as_view(), name='get_data'),
]
