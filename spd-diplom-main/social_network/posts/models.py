from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import ForeignKey
from django.utils import timezone
from datetime import datetime
from django.db.models import Count,Max,Min,Avg

from psycopg2.errorcodes import NULL_VALUE_NOT_ALLOWED

User = get_user_model()

#Создаём модель Посты с фото
class Post(models.Model):

      text=models.TextField(default='прекрасное фото')
      author = models.ForeignKey(User,verbose_name = 'Пользователь', on_delete=models.CASCADE, blank=True)
      image = models.ImageField(upload_to='static/',verbose_name='Изображение',null=True,default=None)
      created_at=models.DateTimeField(null=True,default=datetime.now)


      def __str__(self):
            return self.text[:50]

      class Meta:
          verbose_name = 'Фотография'
          verbose_name_plural = 'Фотографии'


#Создаём модель Комментарии
class Comment(models.Model):
    text = models.TextField(default='The best')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(null=True, default=datetime.now)


    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

#Создаём модель Лайков
class Like(models.Model):

      user = models.ForeignKey(User, on_delete=models.CASCADE)
      post = models.ForeignKey(Post, on_delete=models.CASCADE)
      #likes_count = like.objects.filter.count(like)


      def __str__(self):
             return f"Like by {self.user} on {self.post}"

      def likes_count(self):
          return self.likes.all().count()

      class Meta:
          verbose_name = 'Лайк'
          verbose_name_plural = 'Лайки'
