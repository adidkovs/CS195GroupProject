# Generated by Django 3.2.7 on 2021-10-10 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_member_librarymember_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitems',
            name='description',
            field=models.CharField(default='NoDescription', max_length=2000, verbose_name='description'),
        ),
    ]
