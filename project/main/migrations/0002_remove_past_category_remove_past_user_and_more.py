# Generated by Django 5.0.6 on 2024-06-04 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='past',
            name='category',
        ),
        migrations.RemoveField(
            model_name='past',
            name='user',
        ),
        migrations.RemoveField(
            model_name='sharedwish',
            name='user',
        ),
        migrations.DeleteModel(
            name='Future',
        ),
        migrations.DeleteModel(
            name='Past',
        ),
        migrations.DeleteModel(
            name='SharedWish',
        ),
    ]
