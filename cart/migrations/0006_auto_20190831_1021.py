# Generated by Django 2.2.1 on 2019-08-31 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20190831_0926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sampleitem',
            old_name='file',
            new_name='file_a',
        ),
        migrations.AddField(
            model_name='sampleitem',
            name='file_b',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]
