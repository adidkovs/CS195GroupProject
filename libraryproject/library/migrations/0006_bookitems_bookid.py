# Generated by Django 3.2.7 on 2021-09-20 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20210920_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookitems',
            name='bookID',
            field=models.IntegerField(default=0, verbose_name='book ID'),
        ),
    ]
