from django.test import TestCase

from goods.services import goods_services
from goods.models import Goods


class GoodsServicesTest(TestCase):
    def setUp(self):
        Goods.objects.create(
            name="кардиган", slug="kardigan", color="pink", main_photo="asdasd"
        )
        Goods.objects.create(
            name="кардиган", slug="kardigan-2", color="pink", main_photo="asdasd"
        )
        Goods.objects.create(
            name="Сумка", slug="symka", color="red", main_photo="asdasd"
        )

    def test_get_goods_data(self):
        """The function return is correct data"""

        goods = Goods.objects.all()

        self.assertQuerysetEqual(goods, goods_services.get_goods_data())

    def test_get_product_with_available_product(self):
        """The function with a product with available slug return is correct data"""

        slug_object = "kardigan"
        goods = Goods.objects.filter(slug=slug_object)

        self.assertQuerysetEqual(goods, goods_services.get_product(slug=slug_object))

    def test_get_product_without_product(self):
        """The function with a product with availabale slug return is correct data"""

        slug_object = "no product"
        goods = Goods.objects.filter(slug=slug_object)

        self.assertQuerysetEqual(goods, goods_services.get_product(slug=slug_object))

    def test_get_all_goods_for_name_with_product_name(self):
        """The function with a product name return is correct data"""

        product_name = "кардиган"
        goods = Goods.objects.filter(name=product_name)

        self.assertQuerysetEqual(goods, goods_services.get_all_goods_for_name(product_name))
    
    def test_get_all_goods_for_name_without_product_name(self):
        """The function without a product name return is correct data"""

        product_name = ""
        goods = Goods.objects.filter(name=product_name)

        self.assertQuerysetEqual(goods, goods_services.get_all_goods_for_name(product_name))
    
    def test_get_all_names_goods(self):
        """The function return all names in databses"""
        
        names_goods = Goods.objects.order_by('name').distinct('name')

        self.assertQuerysetEqual(names_goods, goods_services.get_all_names_goods())
    
    def test_get_search_goods_with_name_product(self):
        """The function return all goods by the name you are looking for"""

        name_product = Goods.objects.first()
        search_goods = Goods.objects.filter(name__icontains=name_product)
        
        self.assertQuerysetEqual(search_goods, goods_services.get_search_goods(name_product))

    def test_get_search_goods_without_name_product(self):
        """The function return data without name product"""

        name_product = "Штаны"
        search_goods = Goods.objects.filter(name__icontains=name_product)
        
        self.assertQuerysetEqual(search_goods, goods_services.get_search_goods(name_product))