from django.db.models import Max, Min

from core.models import (
    Address,
    CartOrder,
    CartOrderItems,
    Category,
    Product,
    ProductImages,
    ProductReview,
    Vendor,
    Wishlist,
)


def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()
    min_max_price = Product.objects.aggregate(min_price=Min("price"),max_price=Max("price"))
    try:
            address = Address.objects.filter(user=request.user)

    except:
            address = None

    return {
        "categories": categories,
        "address": address,
        "vendors": vendors,
        'min_max_price': {
            'price__min': min_max_price['min_price'],
            'price__max': min_max_price['max_price']
        }
    }
