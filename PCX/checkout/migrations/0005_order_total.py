# Generated by Django 3.1.2 on 2020-12-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20201203_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
