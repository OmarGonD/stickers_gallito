# Generated by Django 2.2.1 on 2019-09-02 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0004_auto_20190902_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='used_cupons',
            name='cupon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.Cupons'),
        ),
    ]
