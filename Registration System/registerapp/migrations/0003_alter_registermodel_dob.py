# Generated by Django 4.0.6 on 2022-07-30 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0002_registermodel_course_registermodel_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodel',
            name='dob',
            field=models.DateField(default='2002-05-26'),
        ),
    ]
