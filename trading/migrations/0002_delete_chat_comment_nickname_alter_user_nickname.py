# Generated by Django 4.0.1 on 2022-02-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.AddField(
            model_name='comment',
            name='nickname',
            field=models.CharField(default='ABC', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='ABC', max_length=10),
        ),
    ]
