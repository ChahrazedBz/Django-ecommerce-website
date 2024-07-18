from django.shortcuts import render

from core.models import Product


def index(request):
    products = Product.objects.filter(featured=True, product_status="published")
    latest_products = Product.objects.filter(
        featured=True, product_status="published"
    ).order_by("-id")[:6]
    context = {
        "products": products,
        "latest_products": latest_products,
    }
    return render(request, "core/index.html", context)


def product_list_view(request):
    products = Product.objects.filter(product_status="published")

    context = {"products": products}
    return render(request, "core/product-list.html", context)
