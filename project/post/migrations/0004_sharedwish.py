# Generated by Django 5.0.6 on 2024-06-23 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_rename_sharedwish_mywish'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedWish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_wish', to='post.mywish')),
            ],
        ),
    ]
