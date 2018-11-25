# Generated by Django 2.1.3 on 2018-11-25 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.CharField(max_length=12, verbose_name='Sygnatura')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data rozpoczęcia')),
                ('course_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.CourseType', verbose_name='Typ kursu')),
            ],
            options={
                'verbose_name': 'Grupa',
                'verbose_name_plural': 'Grupy',
            },
        ),
    ]
