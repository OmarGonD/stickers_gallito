# Generated by Django 2.2.1 on 2019-09-02 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0005_auto_20190902_1713'),
        ('order', '0003_auto_20190715_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cupon',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketing.Cupons'),
        ),
    ]
