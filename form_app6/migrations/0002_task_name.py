# Generated by Django 4.2.7 on 2023-12-07 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app5', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default=2, max_length=64),
            preserve_default=False,
        ),
    ]
