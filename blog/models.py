from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS = (
    (0,"Rascunho"),
    (1,"Publicado")
)


class Post(models.Model):
    titulo = models.CharField(max_length=155)
    subtitulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', null=False)
    post = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
