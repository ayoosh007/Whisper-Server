import torch
import whisper
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AudioSerializer
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

class Transcriber(APIView):
    def post(self,request,*args,**kwargs):
        serializer = AudioSerializer(data=request.data)
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        model = whisper.load_model("base",device=device)
        if serializer.is_valid():
            audio_file = serializer.validated_data['file']
            path = default_storage.save(r'temp_audio.wav',ContentFile(audio_file.read()))
            result = model.transcribe(default_storage.path(path))

            return Response({'transcript':result['text']},status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
