# Generated by Django 2.2.1 on 2019-07-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20190521_0947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='file',
            new_name='file_a',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='file_b',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]