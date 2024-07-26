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
    try:
        address = Address.objects.filter(user=request.user)
    except:
        address=None
    return {"categories": categories,"address":address}
