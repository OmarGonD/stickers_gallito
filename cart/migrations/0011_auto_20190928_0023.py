# Generated by Django 2.2.1 on 2019-09-28 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_auto_20190917_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.CharField(choices=[('10', '10'), ('20', '20'), ('50', '50'), ('100', '100'), ('200', '200'), ('300', '300'), ('500', '500'), ('1000', '1000'), ('2000', '2000')], max_length=20),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='size',
            field=models.CharField(choices=[('varios', 'varios'), ('3cm x 3cm', '3 cm x 3 cm'), ('5cm x 5cm', '5 cm x 5 cm'), ('7cm x 7cm', '7 cm x 7 cm'), ('10cm x 10cm', '10 cm x 10 cm'), ('13cm x 13cm', '13 cm x 13 cm'), ('15cm x 15cm', '15 cm x 15 cm')], max_length=20),
        ),
        migrations.AlterField(
            model_name='sampleitem',
            name='quantity',
            field=models.CharField(choices=[('10', '10'), ('20', '20'), ('50', '50'), ('100', '100'), ('200', '200'), ('300', '300'), ('500', '500'), ('1000', '1000'), ('2000', '2000')], max_length=20),
        ),
        migrations.AlterField(
            model_name='sampleitem',
            name='size',
            field=models.CharField(choices=[('varios', 'varios'), ('3cm x 3cm', '3 cm x 3 cm'), ('5cm x 5cm', '5 cm x 5 cm'), ('7cm x 7cm', '7 cm x 7 cm'), ('10cm x 10cm', '10 cm x 10 cm'), ('13cm x 13cm', '13 cm x 13 cm'), ('15cm x 15cm', '15 cm x 15 cm')], max_length=20),
        ),
    ]
