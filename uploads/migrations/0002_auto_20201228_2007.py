# Generated by Django 2.2 on 2020-12-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
