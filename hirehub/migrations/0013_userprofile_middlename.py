# Generated by Django 5.1.3 on 2024-12-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hirehub', '0012_alter_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='middlename',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]