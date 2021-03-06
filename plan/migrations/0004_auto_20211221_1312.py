# Generated by Django 3.2.9 on 2021-12-21 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_plan_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='days',
        ),
        migrations.CreateModel(
            name='Lekcja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('prowadzacy', models.CharField(max_length=200)),
                ('dzien', models.CharField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], max_length=20)),
                ('godzinarozpoczecia', models.TimeField()),
                ('godzinazakonczeniaa', models.TimeField()),
                ('rodzaj', models.CharField(choices=[(0, 'Wyk'), (1, 'Lab'), (2, 'Cw')], max_length=10)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.plan')),
            ],
        ),
    ]
