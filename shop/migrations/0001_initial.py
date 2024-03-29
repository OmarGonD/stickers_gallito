# Generated by Django 2.1.3 on 2019-05-21 00:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Peru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('distrito', models.CharField(max_length=100)),
                ('costo_despacho_con_recojo', models.IntegerField(default=15)),
                ('costo_despacho_sin_recojo', models.IntegerField(default=15)),
                ('dias_despacho', models.IntegerField(default=4)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('sku', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product_Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=250, unique=True)),
                ('stars', models.DecimalField(decimal_places=2, max_digits=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductsPricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('5cm x 5cm', '5 cm x 5 cm'), ('7cm x 7cm', '7 cm x 7 cm'), ('10cm x 10cm', '10 cm x 10 cm'), ('13cm x 13cm', '13 cm x 13 cm')], max_length=20)),
                ('quantity', models.CharField(choices=[('50', '50'), ('100', '100'), ('200', '200'), ('300', '300'), ('500', '500'), ('1000', '1000'), ('2000', '2000'), ('3000', '3000'), ('4000', '4000'), ('5000', '5000'), ('10000', '10000')], max_length=20)),
                ('price', models.IntegerField(default=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('dni', models.CharField(blank=True, max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=30)),
                ('shipping_address1', models.CharField(max_length=100)),
                ('reference', models.CharField(max_length=100)),
                ('shipping_department', models.CharField(max_length=100)),
                ('shipping_province', models.CharField(max_length=100)),
                ('shipping_district', models.CharField(max_length=100)),
                ('photo', models.ImageField(default='profile_pics/default_profile_pic_white.png', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('sku', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='sample_images')),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
            options={
                'verbose_name': 'sample',
                'verbose_name_plural': 'samples',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Sample_Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=250, unique=True)),
                ('stars', models.DecimalField(decimal_places=2, max_digits=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Sample')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SamplesPricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('5cm x 5cm', '5 cm x 5 cm'), ('7cm x 7cm', '7 cm x 7 cm'), ('10cm x 10cm', '10 cm x 10 cm'), ('13cm x 13cm', '13 cm x 13 cm')], max_length=20)),
                ('quantity', models.CharField(choices=[('50', '50'), ('100', '100'), ('200', '200'), ('300', '300'), ('500', '500'), ('1000', '1000'), ('2000', '2000'), ('3000', '3000'), ('4000', '4000'), ('5000', '5000'), ('10000', '10000')], max_length=20)),
                ('price', models.IntegerField(default=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Sample')),
            ],
        ),
    ]
