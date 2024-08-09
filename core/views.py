from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from taggit.models import Tag

from core.forms import ProductReviewForm
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
    latest_products = Product.objects.filter(
        featured=True, product_status="published"
    ).order_by("-id")[:6]
    category = Category.objects.all()
    context = {
        "products": products,
        "latest_products": latest_products,
        "categories": category,
    }
    return render(request, "core/product-list.html", context)


def category_list_view(request):
    category = Category.objects.all()
    context = {
        "categories": category,
    }
    return render(request, "core/category-list.html", context)


def category_product_list_view(request, cid):
    category = get_object_or_404(Category, cid=cid)
    products = Product.objects.filter(product_status="published", category=category)

    context = {"category": category, "products": products}
    return render(request, "core/category-product-list.html", context)


def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {"vendors": vendors}
    return render(request, "core/vendor-list.html", context)


def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor, product_status="published")
    context = {"vendor": vendor, "products": products}
    return render(request, "core/vendor-detail.html", context)


def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    p_images = product.p_images.all()
    products = Product.objects.filter(category=product.category).exclude(pid=pid)

    # Getting all reviews
    reviews = ProductReview.objects.filter(product=product).order_by("-date")

    # Getting avg reviews
    average_rating = ProductReview.objects.filter(product=product).aggregate(
        rating=Avg("rating")
    )
    # Product Review Form
    review_form = ProductReviewForm()
    make_review=True
    if request.user.is_authenticated:
        user_review_count=ProductReview.objects.filter(user=request.user,product=product).count()
        if user_review_count >0:
            make_review=False
    context = {
        "review_form": review_form,
        "make_review":make_review,
        "p": product,
        "p_img": p_images,
        "products": products,
        "reviews": reviews,
        "average_rating": average_rating,
        "review_form": review_form,
    }
    return render(request, "core/product-detail.html", context)


def tag_list(request, tag_slug=None):
    products = Product.objects.filter(product_status="published").order_by("-id")
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])
    context = {
        "products": products,
        "tag": tag,
    }
    return render(request, "core/tag.html", context)


def ajax_add_review(request, pid):
    product = Product.objects.get(pk=pid)
    user = request.user

    review=ProductReview.objects.create(
        user=user,
        product=product ,
        review=request.POST['review'],
        rating=request.POST['rating'],

    )
    context={
        'user':user.username,
        'review':request.POST['review'],
        'rating':request.POST['rating'],
    }
    average_reviews=ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    return JsonResponse(
        {
        'bool':True,
        'context':context,
        'average_reviews':average_reviews
        }
    )

def search_view(request):
    query=request.GET["q"]
    products=Product.objects.filter(title__icontains=query).order_by("-date")
    context={
        "products":products,
        "query":query,
    }
    return render(request,"core/search.html",context)
