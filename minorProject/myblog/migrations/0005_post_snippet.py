# Generated by Django 2.2.12 on 2020-10-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_auto_20201030_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='contnue reading', max_length=255),
        ),
    ]
