# Generated by Django 5.0.2 on 2025-02-14 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_message_post_message_user_alter_post_1_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post_1',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
