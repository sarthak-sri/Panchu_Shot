# Generated by Django 2.0 on 2022-09-14 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_caption', models.CharField(default='', help_text='enter a caption', max_length=500)),
                ('post_img', models.ImageField(default='', upload_to='Websit/media')),
                ('post_hashtag', models.CharField(default='', max_length=100)),
            ],
        ),
    ]