# Generated by Django 3.1 on 2020-08-21 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]