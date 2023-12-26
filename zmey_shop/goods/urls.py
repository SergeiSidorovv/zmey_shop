from django.urls import path

from goods import views


urlpatterns = [
    path("", views.AllGoods.as_view(), name="goods"),
    path("product/<slug:product_slug>/", views.Product.as_view(), name="product"),
]
