from django.core.exceptions import ValidationError
from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile


def validations(file: InMemoryUploadedFile) -> None:
    if file.name and 'virus' in file.name:
        raise ValidationError('its virus')


class UploadFile(forms.Form):
    file = forms.FileField(validators=[validations])

