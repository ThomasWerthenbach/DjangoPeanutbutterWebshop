# Generated by Django 3.0.3 on 2020-02-07 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0003_auto_20200207_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='grade',
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField(default=1.0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lecture.Student')),
            ],
        ),
    ]
