# Generated by Django 3.0.8 on 2020-07-21 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('head0', models.CharField(default='', max_length=1000)),
                ('head1', models.CharField(default='', max_length=1000)),
                ('head2', models.CharField(default='', max_length=1000)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
