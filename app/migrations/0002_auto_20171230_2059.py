# Generated by Django 2.0 on 2017-12-30 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='relase_date',
            field=models.DateTimeField(null=True),
        ),
    ]