from django.db import models

from apps.account.models import Profile


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Blog(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=303)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    image = models.ImageField()
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='tags')
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SubText(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, related_name='subtext', null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class SubPicture(models.Model):
    blog_text = models.ForeignKey(SubText, on_delete=models.CASCADE, related_name='subpicture')
    image = models.ImageField('subpicture/')
    is_vite = models.BooleanField(default=True)


class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    description = models.TextField(max_length=303, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
