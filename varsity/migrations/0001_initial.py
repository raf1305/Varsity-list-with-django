# Generated by Django 3.0.8 on 2020-07-25 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Varsity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('univarsity_name', models.CharField(max_length=100)),
                ('univarsity_nickname', models.CharField(max_length=10)),
                ('foundation', models.IntegerField()),
                ('location', models.CharField(max_length=20)),
                ('division', models.CharField(max_length=20)),
                ('specailization', models.CharField(max_length=50)),
                ('phdgranting', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
    ]
