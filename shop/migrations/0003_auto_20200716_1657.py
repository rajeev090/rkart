# Generated by Django 3.0.8 on 2020-07-16 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200715_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='short_desc',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='catagory',
            field=models.CharField(choices=[('appliances', 'Appliances'), ('baby', 'Baby'), ('beauty', 'Beauty'), ('books', 'Books'), ('car', 'Car & Bikes'), ('clothing', 'Clothings & Accessories'), ('collectibles', 'Collectibles'), ('computer', 'Computer & Accessories'), ('electronics', 'Electronics'), ('furniture', 'Furniture')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcatagory',
            field=models.CharField(choices=[('audio', 'Audio Devices'), ('babycare', 'Baby Care'), ('babyclothing', 'Baby Clothings'), ('babytoys', 'Activity & toys'), ('bikeparts', 'Bike Parts & Accessories'), ('carparts', 'Car Parts & Accessories'), ('computerparts', 'Computer Parts & Accessories'), ('cooling', 'Cooling Applinces'), ('desktop', 'Desktops'), ('engnovel', 'English Novel'), ('entertainmentc', 'Entertainment Collectibles'), ('haircare', 'Hair Care'), ('hindinovel', 'Hindi Novel'), ('home', 'Home Appliances'), ('home', 'Home Furniture'), ('kids', 'Kids'), ('kitchen', 'Kitchen Appliances'), ('laptop', 'Laptops'), ('makeup', 'Makup'), ('men', 'Men'), ('mobile', 'Mobile'), ('office', 'Office Furniture'), ('programming', 'Programming'), ('skincare', 'Skin Care'), ('sportsc', 'Sports Collectibles'), ('tv', 'TV'), ('women', 'Women')], max_length=50),
        ),
    ]