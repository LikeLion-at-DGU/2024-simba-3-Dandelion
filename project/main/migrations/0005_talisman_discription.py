# Generated by Django 5.0.6 on 2024-06-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_talisman_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='talisman',
            name='discription',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]