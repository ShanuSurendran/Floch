# Generated by Django 4.2 on 2023-05-01 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-10-22'),
            preserve_default=False,
        ),
    ]