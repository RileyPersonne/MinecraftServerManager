# Generated by Django 5.0.4 on 2024-04-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MinecraftServerManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='status',
            field=models.CharField(default='Start', max_length=16),
            preserve_default=False,
        ),
    ]
