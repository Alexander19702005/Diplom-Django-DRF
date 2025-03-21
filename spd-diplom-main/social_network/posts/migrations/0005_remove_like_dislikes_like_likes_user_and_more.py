# Generated by Django 4.1.13 on 2025-01-31 16:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_alter_post_options_comment_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='dislikes',
        ),
        migrations.AddField(
            model_name='like',
            name='likes_user',
            field=models.ManyToManyField(blank=True, related_name='нравится', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_user',
            field=models.ManyToManyField(blank=True, related_name='коммент', to=settings.AUTH_USER_MODEL),
        ),
    ]
