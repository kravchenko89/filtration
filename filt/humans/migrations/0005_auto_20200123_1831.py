# Generated by Django 2.2.9 on 2020-01-23 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humans', '0004_remove_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]