# Generated by Django 3.0.3 on 2020-02-07 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0004_auto_20200207_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.FloatField(default=1.0),
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]
