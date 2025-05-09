# Generated by Django 5.2 on 2025-05-05 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_is_staff_alter_customuser_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('patient', 'Patient'), ('doctor', 'Doctor'), (
                'pharmacist', 'Pharmacist'), ('admin', 'Admin')], default='patient', max_length=15),
        ),
    ]
