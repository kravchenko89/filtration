# Generated by Django 2.2.9 on 2020-01-11 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humans', '0002_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='curator',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

# def forward(apps, schema_editor):
#     Student = apps.get_model('students', 'Student')
#     for student in Student.objects.all().only('id', 'phone').iterator():
#         student.phone = ''.join(x for x in student.phone if x.isdigit())
#         student.save(update_fields=['phone'])
#
#
#
#     operations = [
#         migrations.RunPython(forward),
#     ]
