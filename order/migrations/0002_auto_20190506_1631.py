# Generated by Django 2.1.3 on 2019-05-06 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='shipping_address2',
            new_name='reference',
        ),
    ]
