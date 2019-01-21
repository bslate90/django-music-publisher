# Generated by Django 2.1.4 on 2019-01-21 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_publisher', '0019_auto_20181227_1504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albumcd',
            options={'ordering': ('album_title', 'cd_identifier', '-id'), 'verbose_name': 'Album and/or Library CD', 'verbose_name_plural': ' Albums and Library CDs'},
        ),
        migrations.AlterModelOptions(
            name='writer',
            options={'ordering': ('last_name', 'first_name', 'ipi_name', '-id'), 'verbose_name_plural': ' Writers'},
        ),
        migrations.AlterModelOptions(
            name='writerinwork',
            options={'ordering': ('-controlled', 'writer__last_name', 'writer__first_name', '-id'), 'verbose_name_plural': 'Writers in Work'},
        ),
    ]
