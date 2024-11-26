from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NumberSerializer
from .models import Number
from django.db.models import F
from django.utils import timezone
from datetime import timedelta
import logging

logger = logging.getLogger('processor')

class NumberProcessorView(APIView):
    def post(self, request):
        serializer = NumberSerializer(data=request.data)
        if serializer.is_valid():
            number = serializer.validated_data['number']

            if Number.objects.filter(value=number).exists():
                logger.error(f"Number {number} has already been processed.")
                return Response(
                    {"error": "Number has already been processed."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if Number.objects.filter(value=number + 1).exists():
                logger.error(f"Number {number} is invalid. Number {number + 1} has already been processed.")
                return Response(
                    {"error": f"Invalid number sequence. Number {number + 1} has already been processed."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            Number.objects.create(value=number)

            return Response({"result": number + 1}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
