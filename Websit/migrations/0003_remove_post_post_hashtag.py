# Generated by Django 2.1.5 on 2022-09-21 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Websit', '0002_contactus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_hashtag',
        ),
    ]