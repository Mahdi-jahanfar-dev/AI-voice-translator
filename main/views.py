from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from main.serializers import VoiceDetailSerializer
from main.models import VoiceDetail
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response



class UploadVoiceView(APIView):
    
    permission_classes = [IsAuthenticated]
    seralizer_class = VoiceDetailSerializer
    
    
    @extend_schema(
        request=VoiceDetailSerializer,
        responses={
            200: {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "voice": {"type": "file"},
                    "voice_text": {"type": "string"}
                }
            },
            401: {"type": "object", "properties": {"error": {"type": "string"}}}
        },
        description="upload your voice"
    )
    def post(self, request):
        user = request.user
        serializer_class = self.seralizer_class(data = request.data)
        serializer_class.is_valid(raise_exception=True)
        return Response(serializer_class.data)