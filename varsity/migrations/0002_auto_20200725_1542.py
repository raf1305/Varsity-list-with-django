# Generated by Django 3.0.8 on 2020-07-25 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('varsity', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='varsity',
            name='id',
        ),
        migrations.AddField(
            model_name='varsity',
            name='varsity_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
