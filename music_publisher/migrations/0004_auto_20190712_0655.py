# Generated by Django 2.1.7 on 2019-07-12 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_publisher', '0003_auto_20190712_0652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recording',
            name='record_label',
        ),
        migrations.RenameField(
            model_name='recording',
            old_name='_record_label',
            new_name='record_label',
        ),
    ]
