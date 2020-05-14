import os
from django.core.exceptions import ValidationError


def validate_audio_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp3', '.wav', '.ogg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension! Upload a mp3 song please.') 

def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension! Upload a .jpg. jpeg. or a .png image')