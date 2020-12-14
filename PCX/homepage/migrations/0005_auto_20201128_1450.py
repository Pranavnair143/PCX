# Generated by Django 3.1.2 on 2020-11-28 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20201127_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_review',
            name='rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product_review',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homepage.product_full'),
        ),
        migrations.DeleteModel(
            name='myrating',
        ),
    ]