# Generated by Django 4.2 on 2023-07-26 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_user_content_user_bio_user_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
