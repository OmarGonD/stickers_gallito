# Generated by Django 4.2.5 on 2023-09-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_ordersummary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
