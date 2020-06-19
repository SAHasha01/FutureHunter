# Generated by Django 3.0.7 on 2020-06-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0006_auto_20200619_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('reading', models.CharField(max_length=50)),
                ('marks', models.CharField(max_length=50)),
                ('virtue', models.CharField(max_length=50)),
                ('interested', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Commerce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('reading', models.CharField(max_length=50)),
                ('marks', models.CharField(max_length=50)),
                ('virtue', models.CharField(max_length=50)),
                ('interested', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Science',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('reading', models.CharField(max_length=50)),
                ('marks', models.CharField(max_length=50)),
                ('virtue', models.CharField(max_length=50)),
                ('interested', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='secondary',
        ),
    ]
