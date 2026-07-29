from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckAPIView(APIView):

    permission_classes = []

    authentication_classes = []

    def get(self, request):

        return Response({

            "status": "success",

            "message": "ERP API is running",

            "version": "1.0.0",
        })