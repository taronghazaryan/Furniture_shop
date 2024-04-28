from django.db import models

from django.contrib.auth.models import User

# Create your models here.


def blogs_image_upload_path(instance: 'Blog', filename: str) -> str:
    return f'blog/{instance.user.username}/{instance.name}/images/{filename}'


class Blog(models.Model):

    class Meta:
        pass

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=30, blank=False, null=False)
    blog_text = models.TextField()
    created_at = models.DateField(auto_now=True)
    image = models.ImageField(blank=True, null=True, upload_to=blogs_image_upload_path)


