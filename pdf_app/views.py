# pdf_app/views.py
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UploadFileSerializer
from .pdfProcessor import *
from .database import *
from django.views import View

class ExtractPDFView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid():
            pdf_file = serializer.validated_data['pdf_file']
            # Use the pdf_processor module to process the PDF
            result = process_pdf(pdf_file)
            # Create the table if not exists
            create_table_if_not_exists()
            # Insert data into the table
            insert_data(result)
            # Return the result as JSON response
            return Response({'result': result}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GetDemoDataView(View):
    def get(self, request, *args, **kwargs):
        try:
            result =get_demo_data(request)
            # print(result)
            # Return the data as JSON response
            return JsonResponse({'data': result}, safe=False)
        except Exception as e :
            return Response(e,  status=status.HTTP_400_BAD_REQUEST)
        
