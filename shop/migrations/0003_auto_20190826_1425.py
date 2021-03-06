# Generated by Django 2.2.1 on 2019-08-26 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190617_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productspricing',
            name='quantity',
            field=models.CharField(choices=[('10', '10'), ('20', '20'), ('50', '50'), ('100', '100'), ('200', '200'), ('300', '300'), ('500', '500'), ('1000', '1000'), ('2000', '2000'), ('3000', '3000'), ('4000', '4000'), ('5000', '5000'), ('10000', '10000')], max_length=20),
        ),
        migrations.AlterField(
            model_name='samplespricing',
            name='quantity',
            field=models.CharField(choices=[('10', '10'), ('20', '20'), ('50', '50'), ('100', '100'), ('200', '200'), ('300', '300'), ('500', '500'), ('1000', '1000'), ('2000', '2000'), ('3000', '3000'), ('4000', '4000'), ('5000', '5000'), ('10000', '10000')], max_length=20),
        ),
    ]
