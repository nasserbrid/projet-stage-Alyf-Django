# Generated by Django 5.1.1 on 2024-09-26 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_planning_alyf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formateur',
            name='user',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Formateur',
        ),
    ]
