# Generated by Django 2.2.2 on 2020-04-08 02:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Kaldi_speech', '0041_remove_user_attend_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userattendance',
            name='attend_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='打卡时间'),
        ),
    ]
