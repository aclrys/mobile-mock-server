# Generated by Django 2.2.1 on 2019-12-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logmodel',
            name='date',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
    ]
