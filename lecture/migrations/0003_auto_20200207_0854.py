# Generated by Django 3.0.3 on 2020-02-07 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0002_student_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.FloatField(default=1.0),
        ),
    ]
