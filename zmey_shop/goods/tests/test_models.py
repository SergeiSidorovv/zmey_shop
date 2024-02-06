from django.test import TestCase

from goods.models import Goods


class GoodsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Goods.objects.create(
            name="кардиган", slug="kardigan", color="pink", main_photo="asdasd"
        )
        Goods.objects.create(
            name="Шапка", slug="Shapka", color="red", main_photo="IMG_R_0067.JPG"
        )

    def test_name_label(self):
        """The name label is written correctly"""

        product = Goods.objects.first()
        field_label = product._meta.get_field("name").verbose_name

        self.assertEqual(field_label, "Имя")

    def test_slug_label(self):
        """The slug label is written correctly"""

        product = Goods.objects.get(slug="Shapka")
        field_label = product._meta.get_field("slug").verbose_name

        self.assertEqual(field_label, "URL")

    def test_color_label(self):
        """The color label is written correctly"""

        product = Goods.objects.get(slug="kardigan")
        field_label = product._meta.get_field("color").verbose_name

        self.assertEqual(field_label, "Цвет")

    def test_main_photo_label(self):
        """The main photo label is written correctly"""

        product = Goods.objects.last()
        field_label = product._meta.get_field("main_photo").verbose_name

        self.assertEqual(field_label, "Основное_фото")

    def test_name_max_length(self):
        """The name length is written correctly"""

        product = Goods.objects.first()
        length = product._meta.get_field("name").max_length

        self.assertEqual(length, 60)

    def test_slug_max_length(self):
        """The slug length is written correctly"""

        product = Goods.objects.get(slug="kardigan")
        length = product._meta.get_field("slug").max_length

        self.assertEqual(length, 60)

    def test_color_max_length(self):
        """The color length is written correctly"""

        product = Goods.objects.get(slug="Shapka")
        length = product._meta.get_field("color").max_length

        self.assertEqual(length, 60)

    def test_str_object_name(self):
        """The object is written correctly"""

        product = Goods.objects.get(slug="Shapka")
        str_object_name = str(product)

        self.assertEqual(str_object_name, "Шапка")

    def test_get_absolute_url(self):
        """The absolute url returned is correct"""

        product = Goods.objects.get(slug="kardigan")
        absolute_url = product.get_absolute_url()

        self.assertEqual(absolute_url, "/product/kardigan/")

    def test_verbose_name_meta(self):
        """The verbose name in meta written is correct"""

        product = Goods.objects.last()
        verbose_name_goods = product._meta.verbose_name

        self.assertEqual(verbose_name_goods, "Одежда")

    def test_verbose_name_plural_meta(self):
        """The verbose name plural in meta written is correct"""

        product = Goods.objects.first()
        verbose_name_plural_goods = product._meta.verbose_name_plural

        self.assertEqual(verbose_name_plural_goods, "Одежды")

    def test_ordering_meta(self):
        """The ordering in meta written is correct"""

        product = Goods.objects.first()
        ordering_goods = product._meta.ordering

        self.assertEqual(ordering_goods, ["id"])
