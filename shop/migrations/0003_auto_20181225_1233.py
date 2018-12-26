# Generated by Django 2.1.3 on 2018-12-25 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_profile_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('distrito', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='shipping_district',
            field=models.CharField(default='mi_distrito', max_length=100),
            preserve_default=False,
        ),
    ]
