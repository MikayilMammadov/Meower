# Generated by Django 4.2 on 2023-07-26 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]