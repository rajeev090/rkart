
def cat():
    cat_list = [
        ('electronics', 'Electronics'),
        ('books', 'Books'),
        ('appliances', 'Appliances'),
        ('baby', 'Baby'),
        ('beauty', 'Beauty'),
        ('car', 'Car & Bikes'),
        ('clothing', 'Clothings & Accessories'),
        ('collectibles', 'Collectibles'),
        ('computer', 'Computer & Accessories'),
        ('furniture', 'Furniture'),
        ('garden', 'Garden & Outdoors'),
        ('health', 'Health & Personal Care'),
        ('home', 'Home & Kitchen'),
        ('industrial', 'Industrial & Scientific'),
        ('jewellery', 'Jewellery'),
        ('luggage', 'Luggage & Bags'),
        ('luxurybeauty', 'Luxury Beauty'),
    ]
    cat_list.sort(key=lambda x: x[0])
    return cat_list


def sub_cat():
    subcat_list = [
        ('tv', 'TV'),
        ('audio', 'Audio Devices'),
        ('mobile', 'Mobile'),
        ('hindinovel', 'Hindi Novel'),
        ('engnovel', 'English Novel'),
        ('programming', 'Programming'),
        ('kitchen', 'Kitchen Appliances'),
        ('cooling', 'Cooling Applinces'),
        ('home', 'Home Appliances'),
        ('babyclothing', 'Baby Clothings'),
        ('babycare', 'Baby Care'),
        ('babytoys', 'Activity & toys'),
        ('makeup', 'Makeup'),
        ('skincare', 'Skin Care'),
        ('haircare', 'Hair Care'),
        ('carparts', 'Car Parts & Accessories'),
        ('bikeparts', 'Bike Parts & Accessories'),
        ('men', 'Men'),
        ('women', 'Women'),
        ('kids', 'Kids'),
        ('sportsc', 'Sports Collectibles'),
        ('entertainmentc', 'Entertainment Collectibles'),
        ('desktop', 'Desktops'),
        ('laptop', 'Laptops'),
        ('computerparts', 'Computer Parts & Accessories'),
        ('office', 'Office Furniture'),
        ('home', 'Home Furniture'),
    ]
    subcat_list.sort(key=lambda x: x[0])
    return subcat_list


def tags():
    tag_list = []
    a = cat()
    b = sub_cat()
    for i in a:
        tag_list.append(i)
    for i in b:
        tag_list.append(i)
    return tag_list
