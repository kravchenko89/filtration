# Generated by Django 2.2.9 on 2020-01-23 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humans', '0006_remove_group_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
