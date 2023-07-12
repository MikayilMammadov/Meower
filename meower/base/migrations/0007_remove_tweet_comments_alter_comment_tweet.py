# Generated by Django 4.2 on 2023-07-12 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_user_comment_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='comments',
        ),
        migrations.AlterField(
            model_name='comment',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='base.tweet'),
        ),
    ]