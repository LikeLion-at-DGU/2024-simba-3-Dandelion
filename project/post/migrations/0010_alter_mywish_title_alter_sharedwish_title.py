# Generated by Django 5.0.6 on 2024-06-26 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_remove_mywish_like_remove_sharedwish_like_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywish',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sharedwish',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
