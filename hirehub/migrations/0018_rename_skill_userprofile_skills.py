# Generated by Django 5.1.3 on 2024-12-14 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hirehub', '0017_alter_userprofile_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='skill',
            new_name='skills',
        ),
    ]
