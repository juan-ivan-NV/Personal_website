# Generated by Django 3.1.3 on 2021-01-04 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210103_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]