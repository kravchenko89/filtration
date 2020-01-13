# Generated by Django 2.2.9 on 2020-01-11 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('lesson', models.CharField(max_length=100)),
                ('curator', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=16)),
            ],
        ),
    ]