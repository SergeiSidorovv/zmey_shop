from django.urls import path

from goods.views import AllGoods, Product


urlpatterns = [
    path("", AllGoods.as_view(), name="goods"),
    path("product/<slug:product_slug>/", Product.as_view(), name="product"),
]
