# Generated by Django 5.0.2 on 2025-02-15 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_rename_post_post_1_image_alter_post_1_text_1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_1',
            old_name='image',
            new_name='post',
        ),
        migrations.AlterField(
            model_name='post_1',
            name='text_1',
            field=models.TextField(default='The best', max_length=500),
        ),
    ]
