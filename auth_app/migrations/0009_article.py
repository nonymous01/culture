# Generated by Django 4.2.5 on 2024-11-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0008_servicerequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=200)),
                ('titre', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
