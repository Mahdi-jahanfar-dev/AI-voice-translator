from main.models import VoiceDetail
from rest_framework import serializers



class VoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceDetail
        fields = ['id', 'title', 'voice', 'voice_text']