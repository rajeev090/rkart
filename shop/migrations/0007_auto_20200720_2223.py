# Generated by Django 3.0.8 on 2020-07-20 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200720_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.CharField(default='', max_length=50),
        ),
    ]