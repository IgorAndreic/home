# Generated by Django 4.2.11 on 2024-04-26 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='is_root',
            field=models.BooleanField(default=False),
        ),
    ]