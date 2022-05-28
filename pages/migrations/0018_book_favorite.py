# Generated by Django 4.0.4 on 2022-05-24 06:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0017_remove_comment_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]