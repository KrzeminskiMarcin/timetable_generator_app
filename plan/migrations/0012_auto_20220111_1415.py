# Generated by Django 3.2.9 on 2022-01-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0011_lekcja_dlugosc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lekcja',
            name='godzinarozpoczecia',
            field=models.IntegerField(blank=True, choices=[(0, '8:00'), (1, '8:15'), (2, '8:30'), (3, '8:45'), (4, '9:00'), (5, '9:15'), (6, '9:30'), (7, '9:45'), (8, '10:00'), (9, '10:15'), (10, '10:30'), (11, '10:45'), (12, '11:00'), (13, '11:15'), (14, '11:30'), (15, '11:45'), (16, '12:00'), (17, '12:15'), (18, '12:30'), (19, '12:45'), (20, '13:00'), (21, '13:15'), (22, '13:30'), (23, '13:45'), (24, '14:00'), (25, '14:15'), (26, '14:30'), (27, '14:45'), (28, '15:00'), (29, '15:15'), (30, '15:30'), (31, '15:45'), (32, '16:00'), (33, '16:15'), (34, '16:30'), (35, '16:45'), (36, '17:00'), (37, '17:15'), (38, '17:30'), (39, '17:45'), (40, '18:00'), (41, '18:15'), (42, '18:30'), (43, '18:45'), (44, '19:00'), (45, '19:15'), (46, '19:30'), (47, '19:45'), (48, '20:00')]),
        ),
        migrations.AlterField(
            model_name='lekcja',
            name='godzinazakonczeniaa',
            field=models.IntegerField(blank=True, choices=[(0, '8:00'), (1, '8:15'), (2, '8:30'), (3, '8:45'), (4, '9:00'), (5, '9:15'), (6, '9:30'), (7, '9:45'), (8, '10:00'), (9, '10:15'), (10, '10:30'), (11, '10:45'), (12, '11:00'), (13, '11:15'), (14, '11:30'), (15, '11:45'), (16, '12:00'), (17, '12:15'), (18, '12:30'), (19, '12:45'), (20, '13:00'), (21, '13:15'), (22, '13:30'), (23, '13:45'), (24, '14:00'), (25, '14:15'), (26, '14:30'), (27, '14:45'), (28, '15:00'), (29, '15:15'), (30, '15:30'), (31, '15:45'), (32, '16:00'), (33, '16:15'), (34, '16:30'), (35, '16:45'), (36, '17:00'), (37, '17:15'), (38, '17:30'), (39, '17:45'), (40, '18:00'), (41, '18:15'), (42, '18:30'), (43, '18:45'), (44, '19:00'), (45, '19:15'), (46, '19:30'), (47, '19:45'), (48, '20:00')]),
        ),
    ]
