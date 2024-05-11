from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def user_avatar_directory_path(instance: 'Profile', filename: str) -> str:
    return f'accounts/user_{instance.user.pk}/avatar/{filename}'


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    agreement_accepted = models.BooleanField(default=False)
    user_avatar = models.ImageField(null=True, blank=True, upload_to=user_avatar_directory_path)


def user_images_directory_path(instance: 'ProfileImages', filename: str) -> str:
    return f'accounts/user_{instance.user.pk}/images/{filename}'


class ProfileImages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(null=True, blank=True, upload_to=user_images_directory_path)



