# Generated by Django 4.0.4 on 2022-05-06 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_application_scolarship_type_student_applications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='scolarship_type',
            new_name='scholarship_type',
        ),
    ]
