from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from pictures.models import Pictures
from goods.models import Goods


class PicturesModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        product = Goods.objects.create(
            name="кардиган", slug="kardigan", color="pink", main_photo="asdasd"
        )
        Pictures.objects.create(photo="IMG_R_0067.jpg", goods_id=product.id)
        Pictures.objects.create(
            photo="photo_2023-11-19_19-04-03.jpg", goods_id=product.id
        )

    def test_pictures_photo_label(self):
        """The photo label is written correctly"""

        picture_for_product = Pictures.objects.get(photo="IMG_R_0067.jpg")
        field_label = picture_for_product._meta.get_field("photo").verbose_name

        self.assertEqual(field_label, "фото")

    def test_pictures_goods_id_label(self):
        """The goods_id label is written correctly"""

        picture_for_product = Pictures.objects.get(
            photo="photo_2023-11-19_19-04-03.jpg"
        )
        field_label = picture_for_product._meta.get_field("goods").verbose_name

        self.assertEqual(field_label, "id_вещи")

    def test_pictures_str(self):
        """The name one picture is written correctly"""

        picture_for_product = Pictures.objects.get(photo="IMG_R_0067.jpg")
        pictures_str_name = str(picture_for_product)

        self.assertEqual(pictures_str_name, "Фотография")

    def test_pictures_meta(self):
        """The meta data is written correctly"""

        picture_for_product = Pictures.objects.get(id=2)
        pictures_verbose_name = picture_for_product._meta.verbose_name
        pictures_verbose_name_plural = picture_for_product._meta.verbose_name_plural

        self.assertEqual(pictures_verbose_name, "Фотографию")
        self.assertEqual(pictures_verbose_name_plural, "Фотографии")

    def test_pictures_create_photo(self):
        """The create photo is correctly add"""

        photo = SimpleUploadedFile(
            name="IMG_R_0067.JPG",
            content=open("media/test_photo/IMG_R_0067.JPG", "rb").read(),
        )
        self.assertTrue(photo)
