# Generated by Django 3.0.5 on 2020-05-14 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20200514_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, default='settings.MEDIA_ROOT/audio/default.jpg', upload_to='audio/'),
        ),
    ]