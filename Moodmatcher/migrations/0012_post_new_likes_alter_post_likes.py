# Generated by Django 5.0.1 on 2024-02-02 05:17

from django.conf import settings
from django.db import migrations, models


def copy_likes(apps, schema_editor):
    Post = apps.get_model('Moodmatcher', 'Post')
    for post in Post.objects.all():
        post.new_likes = post.likes.count()
        post.save()

class Migration(migrations.Migration):

    dependencies = [
        ('Moodmatcher', '0010_alter_comment_post'),  # 존재하는 이전 마이그레이션 파일 이름으로 변경
    ]

    

    operations = [
        migrations.AddField(
            model_name='post',
            name='new_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
         migrations.RunPython(copy_likes),
    ]