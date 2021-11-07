# Generated by Django 3.2.7 on 2021-11-05 14:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0019_reserved_books_canreserve'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=1000)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.bookitems')),
            ],
        ),
    ]
