# Generated by Django 2.1.3 on 2019-05-06 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=30)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('email', models.EmailField(blank=True, max_length=250, verbose_name='Correo electrónico')),
                ('last_four', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('shipping_address', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping_address1', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping_address2', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping_department', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping_province', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping_district', models.CharField(blank=True, max_length=100, null=True)),
                ('reason', models.CharField(blank=True, default='', max_length=400, null=True)),
                ('status', models.CharField(choices=[('recibido_pagado', 'Recibido y pagado'), ('recibido_no_pagado', 'Recibido pero no pagado'), ('en_proceso', 'En proceso'), ('en_camino', 'En camino'), ('entregado', 'Entregado')], default='recibido_pagado', max_length=20)),
            ],
            options={
                'db_table': 'Order',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='PEN Price')),
                ('file', models.FileField(blank=True, null=True, upload_to='files')),
                ('comment', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
            options={
                'db_table': 'OrderItem',
            },
        ),
    ]
