# Generated by Django 5.0.6 on 2024-06-23 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_past_category_remove_past_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='talisman',
            name='description',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
