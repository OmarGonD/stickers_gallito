# Generated by Django 2.2.1 on 2019-09-17 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_packitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packitem',
            name='quantity',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='packitem',
            name='size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
