# Generated by Django 3.0.8 on 2020-07-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('varsity', '0004_auto_20200725_1549'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='varsity',
            constraint=models.UniqueConstraint(fields=('univarsity_name', 'univarsity_nickname'), name='name_nick'),
        ),
    ]
