# Generated by Django 2.2.12 on 2021-04-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210413_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
