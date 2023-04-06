from django.urls import path
from mainapp.views import index
from mainapp.views import login
from mainapp.views import getProducts
from mainapp.views import getProductDetail
from mainapp.views import reserveProduct,reserveProductCount,reserveProductList,reserve,reserveProductRemove

urlpatterns = [
    path("", index, name="index"),  
    path("reserve", reserve, name="reserve"),    
    path("api/product-get", getProducts, name = "products_get"),
    path("api/product-detail-get", getProductDetail, name = "product_detail_get"),
    path("api/product-reserve", reserveProduct, name = "product_reserve"),
    path("api/product-reserve-count", reserveProductCount, name = "product_reserve_count"),
    path("api/product-reserve-list", reserveProductList, name = "product_reserve_list"),
    path("api/product-reserve-remove", reserveProductRemove, name = "product_reserve_remove")
]