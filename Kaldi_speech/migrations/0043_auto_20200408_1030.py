# Generated by Django 2.2.2 on 2020-04-08 02:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Kaldi_speech', '0042_auto_20200408_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userattendance',
            name='attend_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='打卡时间'),
        ),
    ]