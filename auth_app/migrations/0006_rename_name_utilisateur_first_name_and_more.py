# Generated by Django 4.2.5 on 2024-08-07 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0005_utilisateur_name_utilisateur_prenom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='utilisateur',
            old_name='prenom',
            new_name='last_name',
        ),
    ]