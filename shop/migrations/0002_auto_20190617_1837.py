# Generated by Django 2.2.1 on 2019-06-17 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productspricing',
            name='quantity',
            field=models.CharField(choices=[('5', '5'), ('10', '10'), ('50', '50'), ('100', '100'), ('200', '200'), ('300', '300'), ('500', '500'), ('1000', '1000'), ('2000', '2000'), ('3000', '3000'), ('4000', '4000'), ('5000', '5000'), ('10000', '10000')], max_length=20),
        ),
        migrations.AlterField(
            model_name='productspricing',
            name='size',
            field=models.CharField(choices=[('varios', 'varios'), ('3cm x 3cm', '3 cm x 3 cm'), ('5cm x 5cm', '5 cm x 5 cm'), ('7cm x 7cm', '7 cm x 7 cm'), ('10cm x 10cm', '10 cm x 10 cm'), ('13cm x 13cm', '13 cm x 13 cm')], max_length=20),
        ),
        migrations.AlterField(
            model_name='samplespricing',
            name='quantity',
            field=models.CharField(choices=[('5', '5'), ('10', '10'), ('50', '50'), ('100', '100'), ('200', '200'), ('300', '300'), ('500', '500'), ('1000', '1000'), ('2000', '2000'), ('3000', '3000'), ('4000', '4000'), ('5000', '5000'), ('10000', '10000')], max_length=20),
        ),
        migrations.AlterField(
            model_name='samplespricing',
            name='size',
            field=models.CharField(choices=[('varios', 'varios'), ('3cm x 3cm', '3 cm x 3 cm'), ('5cm x 5cm', '5 cm x 5 cm'), ('7cm x 7cm', '7 cm x 7 cm'), ('10cm x 10cm', '10 cm x 10 cm'), ('13cm x 13cm', '13 cm x 13 cm')], max_length=20),
        ),
    ]
