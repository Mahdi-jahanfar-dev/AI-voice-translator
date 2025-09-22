from django.urls import path
from main.views import UploadVoiceView


urlpatterns = [
    path("voice/upload/", UploadVoiceView.as_view(), name="upload-voice")
]