# Generated by Django 3.0.7 on 2020-06-18 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0002_auto_20200618_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secondarysci',
            name='answer',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]
