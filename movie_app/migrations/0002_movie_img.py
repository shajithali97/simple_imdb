# Generated by Django 3.2.7 on 2021-09-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ssa', upload_to='GALLERY'),
            preserve_default=False,
        ),
    ]