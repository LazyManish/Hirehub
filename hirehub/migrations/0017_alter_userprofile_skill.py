# Generated by Django 5.1.3 on 2024-12-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hirehub', '0016_alter_skill_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='skill',
            field=models.ManyToManyField(related_name='profile', to='hirehub.skill'),
        ),
    ]
