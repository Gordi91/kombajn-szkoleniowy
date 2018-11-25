# Generated by Django 2.1.3 on 2018-11-25 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa')),
                ('module_num', models.PositiveSmallIntegerField(verbose_name='Nr modułu')),
                ('course_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.CourseType', verbose_name='Typ kursu')),
            ],
            options={
                'verbose_name': 'Egzamin',
                'verbose_name_plural': 'Egzaminy',
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveSmallIntegerField(verbose_name='Numer zadania')),
                ('points', models.PositiveSmallIntegerField(verbose_name='Punkty')),
                ('description', models.TextField(verbose_name='Treść zadania')),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.Exam', verbose_name='Egzamin')),
            ],
            options={
                'verbose_name': 'Zadanie',
                'verbose_name_plural': 'Zadania',
            },
        ),
    ]
