# Generated by Django 3.0.7 on 2020-06-18 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secondarysci',
            name='answer',
            field=models.BooleanField(default=True),
        ),
    ]