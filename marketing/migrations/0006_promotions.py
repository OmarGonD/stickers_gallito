# Generated by Django 2.2.1 on 2023-08-14 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0005_auto_20190902_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packs_3x2', models.BooleanField(blank=True, default=False, null=True)),
                ('stickers_unitarios_3x2', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
