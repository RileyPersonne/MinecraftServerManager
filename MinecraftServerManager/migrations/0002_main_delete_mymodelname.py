# Generated by Django 5.0.3 on 2024-04-03 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MinecraftServerManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SERVERNAME', models.CharField(max_length=16)),
            ],
        ),
        migrations.DeleteModel(
            name='MyModelName',
        ),
    ]
