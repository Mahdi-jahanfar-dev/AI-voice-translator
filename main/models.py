from django.db import models


class VoiceDetail(models.Model):   
    title = models.CharField(max_length=200)
    voice = models.FileField(upload_to="audio", null=True, blank=True)
    voice_text = models.TextField()
    

class TranslatedText(models.Model):
    voice = models.ForeignKey(VoiceDetail, on_delete=models.CASCADE, related_name="translates")
    translated_text = models.TextField()
    translated_language = models.CharField(max_length=100)