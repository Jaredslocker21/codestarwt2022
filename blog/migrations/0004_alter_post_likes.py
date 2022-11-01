# Generated by Django 3.2.16 on 2022-11-01 16:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_rename_featuered_image_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='blogpsot_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
