# Generated by Django 3.1.2 on 2020-11-29 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_review',
            name='user',
        ),
    ]
