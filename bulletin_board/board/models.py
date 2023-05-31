from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


NAME_CATEGORY = [  # thanks to yandex translator for the translation
    ('Tanks', 'Танки'),
    ('Frail', 'Хилы'),
    ('DD', 'ДД'),
    ('Merchants', 'Торговцы'),
    ('Guild Masters', 'Гилдмастеры'),
    ('Quest Givers', 'Квестгиверы'),
    ('Blacksmiths', 'Кузнецы'),
    ('Tanners', 'Кожевники'),
    ('Potion Makers', 'Зельевары'),
    ('Spell Masters', 'Мастера заклинаний'),
]

class Post(models.Model):


    title = models.CharField(max_length=254)
    body = RichTextField()
    category = models.CharField(max_length=254, choices=NAME_CATEGORY)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])


RESPONSE_STATUS = [
    ('Accept', 'Принять'),
    ('Delete', 'Удалить'),
]

class Response(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, null=True, choices=RESPONSE_STATUS)
