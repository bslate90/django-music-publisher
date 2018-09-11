# Generated by Django 2.1 on 2018-09-11 10:17

from django.db import migrations, models
import music_publisher.models


class Migration(migrations.Migration):

    dependencies = [
        ('music_publisher', '0006_auto_20180801_2130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albumcd',
            options={'ordering': ('album_title', 'cd_identifier'), 'verbose_name': 'Album and/or Library CD', 'verbose_name_plural': ' Albums and Library CDs'},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': 'Performing Artist', 'verbose_name_plural': ' Performing Artists'},
        ),
        migrations.AlterModelOptions(
            name='cwrexport',
            options={'ordering': ('-id',), 'verbose_name': 'CWR Export', 'verbose_name_plural': 'CWR Exports'},
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'verbose_name_plural': '  Works'},
        ),
        migrations.AlterModelOptions(
            name='workacknowledgement',
            options={'verbose_name': 'Registration Acknowledgement'},
        ),
        migrations.AlterModelOptions(
            name='writer',
            options={'ordering': ('last_name', 'first_name', 'ipi_name'), 'verbose_name_plural': ' Writers'},
        ),
        migrations.AlterModelOptions(
            name='writerinwork',
            options={'ordering': ('-controlled', 'writer__last_name', 'writer__first_name'), 'verbose_name_plural': 'Writers in Work'},
        ),
        migrations.AlterField(
            model_name='work',
            name='last_change',
            field=models.DateTimeField(editable=False, null=True, verbose_name='Last Edited'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='ipi_name',
            field=models.CharField(blank=True, help_text='Required for a controlled writer', max_length=11, null=True, unique=True, validators=[music_publisher.models.CWRFieldValidator('writer_ipi_name')], verbose_name='IPI Name #'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='pr_society',
            field=models.CharField(blank=True, choices=[('101', 'SOCAN, Canada'), ('088', 'CMRRA, Canada'), ('058', 'SACEM, France'), ('068', 'SDRM, France'), ('035', 'GEMA, Germany'), ('074', 'SIAE, Italy'), ('052', 'PRS, United Kingdom'), ('044', 'MCPS, United Kingdom'), ('010', 'ASCAP, United States'), ('021', 'BMI, United States'), ('071', 'SESAC Inc., United States'), ('034', 'HFA, United States')], help_text='Required for a controlled writer', max_length=3, null=True, validators=[music_publisher.models.CWRFieldValidator('writer_pr_society')], verbose_name='Performing Rights Society'),
        ),
    ]
