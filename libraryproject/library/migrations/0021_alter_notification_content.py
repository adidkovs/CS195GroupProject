# Generated by Django 3.2.7 on 2021-11-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0020_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]
