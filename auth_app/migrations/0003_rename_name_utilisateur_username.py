# Generated by Django 4.2.7 on 2023-11-24 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_utilisateur_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='name',
            new_name='username',
        ),
    ]
