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
    address = Address.objects.all(user=request.user)
    return {"categories": categories, "address": address}
