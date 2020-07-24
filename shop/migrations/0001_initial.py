# Generated by Django 3.0.8 on 2020-07-19 14:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', editable=False, max_length=50)),
                ('email', models.CharField(default='', editable=False, max_length=50)),
                ('phone', models.CharField(default='', editable=False, max_length=15)),
                ('msgtype', models.CharField(default='', editable=False, max_length=15)),
                ('message', models.TextField(editable=False)),
                ('date', models.DateField(default=datetime.datetime(2020, 7, 19, 14, 31, 53, 598816, tzinfo=utc), editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('appliances', 'Appliances'), ('baby', 'Baby'), ('beauty', 'Beauty'), ('books', 'Books'), ('car', 'Car & Bikes'), ('clothing', 'Clothings & Accessories'), ('collectibles', 'Collectibles'), ('computer', 'Computer & Accessories'), ('electronics', 'Electronics'), ('furniture', 'Furniture'), ('garden', 'Garden & Outdoors'), ('health', 'Health & Personal Care'), ('home', 'Home & Kitchen'), ('industrial', 'Industrial & Scientific'), ('jewellery', 'Jewellery'), ('luggage', 'Luggage & Bags'), ('luxurybeauty', 'Luxury Beauty')], default='', max_length=50)),
                ('subcategory', models.CharField(choices=[('audio', 'Audio Devices'), ('babycare', 'Baby Care'), ('babyclothing', 'Baby Clothings'), ('babytoys', 'Activity & toys'), ('bikeparts', 'Bike Parts & Accessories'), ('carparts', 'Car Parts & Accessories'), ('computerparts', 'Computer Parts & Accessories'), ('cooling', 'Cooling Applinces'), ('desktop', 'Desktops'), ('engnovel', 'English Novel'), ('entertainmentc', 'Entertainment Collectibles'), ('haircare', 'Hair Care'), ('hindinovel', 'Hindi Novel'), ('home', 'Home Appliances'), ('home', 'Home Furniture'), ('kids', 'Kids'), ('kitchen', 'Kitchen Appliances'), ('laptop', 'Laptops'), ('makeup', 'Makeup'), ('men', 'Men'), ('mobile', 'Mobile'), ('office', 'Office Furniture'), ('programming', 'Programming'), ('skincare', 'Skin Care'), ('sportsc', 'Sports Collectibles'), ('tv', 'TV'), ('women', 'Women')], default='', max_length=50)),
                ('brand', models.CharField(default='', max_length=50)),
                ('desc', models.TextField(max_length=1500)),
                ('price', models.FloatField(default=0)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
