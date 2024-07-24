from django.db import models
from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField
from taggit.managers import TaggableManager

from userauths.models import User

# Choice definitions
################### Choice definitions ###################
STATUS_CHOICE = (
    ("process", "Processing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered"),
)

STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("published", "Published"),
)

RATING = (
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★"),
)


# Utility functions
################### Utility functions ###################
def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


# Category model
################### Category model ###################
class Category(models.Model):
    cid = ShortUUIDField(
        unique=True, length=10, max_length=20, prefix="cat", alphabet="abcdefgk"
    )
    title = models.CharField(max_length=100, default="Food")
    image = models.ImageField(upload_to="category", default="category.jpg")

    class Meta:
        verbose_name_plural = "categories"

    def category_image(self):
        if self.image and hasattr(self.image, "url"):
            return mark_safe(
                '<img src="%s" width="50" height="50" />' % (self.image.url)
            )
        return "No Image"

    def __str__(self):
        return str(self.title)


# Tags model
################### Tags model ###################
class Tags(models.Model):
    pass


# Vendor model
################### Vendor model ###################
class Vendor(models.Model):
    vid = ShortUUIDField(
        unique=True, length=10, max_length=20, prefix="ven", alphabet="abcdefgk"
    )
    title = models.CharField(max_length=100, default="oragi")
    image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
    cover_image = models.ImageField(upload_to=user_directory_path, default="cover.jpg")

    description = models.TextField(null=True, blank=True, default="I'm the best vendor")

    address = models.CharField(max_length=100, default="123 Main street")
    contact = models.CharField(max_length=100, default="+123 (456) 789")
    chat_resp_time = models.CharField(max_length=100, default="100")
    shipping_on_time = models.CharField(max_length=100, default="100")
    authentic_rating = models.CharField(max_length=100, default="100")
    days_return = models.CharField(max_length=100, default="100")
    warranty_period = models.CharField(max_length=100, default="100")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        if self.image and hasattr(self.image, "url"):
            return mark_safe(
                '<img src="%s" width="50" height="50" />' % (self.image.url)
            )
        return "No Image"

    def __str__(self):
        return str(self.title)


# Product model
################### Product model ###################
class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="qbcdefgk")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="category"
    )
    vendor = models.ForeignKey(
        Vendor, on_delete=models.SET_NULL, null=True, related_name="vendor"
    )
    title = models.CharField(max_length=100, default="Fresh Pear")
    image = models.ImageField(upload_to=user_directory_path, default="product.jpg")
    description = models.TextField(null=True, blank=True, default="This is the product")
    price = models.DecimalField(max_digits=10, decimal_places=2, default="1.99")
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default="2.99")
    specification = models.TextField(null=True, blank=True, default="")
    type = models.CharField(max_length=100, default="Organic", null=True, blank=True)
    stock_count = models.CharField(
        max_length=100, default="8 items", null=True, blank=True
    )
    life = models.CharField(max_length=100, default="100 days", null=True, blank=True)
    mfd = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    tags = TaggableManager(blank=True)
    product_status = models.CharField(
        choices=STATUS, max_length=10, default="in_review"
    )
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    sku = ShortUUIDField(
        unique=True, length=4, max_length=10, prefix="sku", alphabet="1234567890"
    )
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    class Meta:
        verbose_name_plural = "products"

    def product_image(self):
        if self.image and hasattr(self.image, "url"):
            return mark_safe(
                '<img src="%s" width="50" height="50" />' % (self.image.url)
            )
        return "No Image"

    def __str__(self):
        return str(self.title)

    def get_percentage(self):
        new_price = ((self.old_price - self.price) / self.old_price) * 100
        return new_price


# Product Images model
################### Product Images model ###################
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product_images", default="product.jpg")
    product = models.ForeignKey(
        Product, related_name="p_images", on_delete=models.SET_NULL, null=True
    )
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Products Images"


# CartOrder model
################### CartOrder model ###################
class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default="1.99")
    paid_track = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(
        choices=STATUS_CHOICE, max_length=30, default="process"
    )

    class Meta:
        verbose_name_plural = "Cart Orders"


# CartOrderItems model
################### CartOrderItems model ###################
class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default="1.99")
    total = models.DecimalField(max_digits=10, decimal_places=2, default="1.99")
    invoice_no = models.CharField(max_length=200, default="default_invoice_no")

    class Meta:
        verbose_name_plural = "Cart Order items"

    def order_img(self):
        if self.image and hasattr(self.image, "url"):
            return mark_safe(
                '<img src="/media/%s" width="50" height="50" />' % (self.image)
            )
        return "No Image"


# Product Review model
################### Product Review model ###################
class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "product Reviews"

    def __str__(self):
        return str(self.product)

    def get_rating(self):
        return self.rating


# Wishlist model
################### Wishlist model ###################
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "wishlists"

    def __str__(self):
        return str(self.product)


# Address model
################### Address model ###################
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Addresses"
