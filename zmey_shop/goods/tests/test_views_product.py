from django.test import TestCase, Client
from django.urls import reverse

from goods import views
from goods.models import Goods
from pictures.models import Pictures


class ProductTest(TestCase):
    def setUp(self):
        self.client = Client()
        Goods.objects.create(
            name="Шапка", slug="Shapka", color="pink", main_photo="asdasd"
        )

    def test_url_status_code(self):
        """The url works correctly when specifying the path"""

        response = self.client.get("/product/Shapka/")

        self.assertEqual(response.status_code, 200)

    def test_url_status_by_name(self):
        """The url works correctly when specifying the namespace"""

        response = self.client.get(
            reverse("product", kwargs={"product_slug": "Shapka"})
        )

        self.assertEqual(response.status_code, 200)
    
    def test_table_used(self):
        """The table in database choice is correct"""

        product_model = views.Product.model
        product = Goods

        self.assertEqual(product_model, product)
    
    def test_template_name(self):
        """The template name is write correct"""

        response = self.client.get("/product/Shapka/")

        self.assertTemplateUsed(response, "goods/product.html")
    
    def test_context_object_name(self):
        """The context object name is write correct"""

        product_view = views.Product()
        context_object_name_product = product_view.context_object_name

        self.assertEqual(context_object_name_product, "product")
    
    def test_context_product_from_get_context_data(self):
        """The context of the product is available in context data"""

        response = self.client.get(reverse("product", kwargs={"product_slug": "Shapka"}))
        context_product = response.context["product"]
        
        self.assertEqual(len(context_product), 1)
    
    def test_context_without_pictures_from_get_context_data(self):
        """Context without data images work correctly in context data"""

        response = self.client.get(reverse("product", kwargs={"product_slug": "Shapka"}))
        context_pictures = response.context["pictures"]
        
        self.assertEqual(len(context_pictures), 0)
    
    def test_context_data_with_pictures(self):
        """Context with data images work correctly in context data"""

        product = Goods.objects.first()
        Pictures.objects.create(
            photo="photo_2023-11-19_19-04-03.jpg", goods_id=product.id
        )
        response = self.client.get(reverse("product", kwargs={"product_slug": "Shapka"}))
        
        context_pictures = response.context["pictures"]
        
        self.assertEqual(len(context_pictures), 1)

