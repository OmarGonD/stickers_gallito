# Generated by Django 2.2.1 on 2019-10-05 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20191004_1405'),
        ('cart', '0012_unitaryproductitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unitaryproductitem',
            name='pack',
        ),
        migrations.AddField(
            model_name='unitaryproductitem',
            name='unitaryproduct',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.UnitaryProduct'),
            preserve_default=False,
        ),
    ]
