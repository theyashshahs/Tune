# Generated by Django 3.0.2 on 2020-04-04 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebTune', '0005_auto_20200404_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='song_file',
            new_name='audio_file',
        ),
    ]
