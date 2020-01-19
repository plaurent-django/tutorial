# Generated by Django 3.0.2 on 2020-01-19 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0009_auto_20200119_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Constants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255, unique=True)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='app',
            name='constants',
            field=models.ManyToManyField(to='tutorial.Constants'),
        ),
    ]