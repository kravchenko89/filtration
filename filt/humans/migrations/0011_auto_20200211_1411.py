# Generated by Django 2.2.9 on 2020-02-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humans', '0010_auto_20200204_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logger',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]
