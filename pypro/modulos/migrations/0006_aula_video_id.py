# Generated by Django 5.2.3 on 2025-07-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='video_id',
            field=models.CharField(default='1', max_length=64),
        ),
    ]
