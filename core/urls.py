from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.product_list_view, name="product-list"),
    path("product/<str:pid>/", views.product_detail_view, name="product-detail"),

    path("categories/", views.category_list_view, name="category-list"),
    path(
        "category/<str:cid>/",
        views.category_product_list_view,
        name="category-product-list",
    ),
    path("vendors/", views.vendor_list_view, name="vendor-list"),
    path("vendor/<str:vid>/", views.vendor_detail_view, name="vendor-detail"),

    #Tags
    path("products/tags/<slug:tag_slug>/",views.tag_list,name="tags"),

    #add review
    path("ajax-add-review/<int:pid>/",views.ajax_add_review,name="ajax_add_review"),

    # Search
    path("search/", views.search_view, name="search"),
    
    path("filter-product/",views.filter_product,name="filter-product")
]
