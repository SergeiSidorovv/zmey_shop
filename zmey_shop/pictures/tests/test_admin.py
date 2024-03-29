from unittest.mock import Mock
from django.test import TestCase
from django.contrib.admin import AdminSite

from pictures.models import Pictures
from pictures.admin import PicturesAdmin


class AdminPicturesTest(TestCase):
    def setUp(self):
        site = AdminSite()
        model_admin = Pictures
        self.admin = PicturesAdmin(model=model_admin, admin_site=site)

    def test_fields(self):
        """The fields are written correctly"""

        fields = self.admin.fields

        self.assertEqual(fields, ["photo", "goods"])

    def test_list_display(self):
        """The list display are written correctly"""

        list_display = self.admin.list_display

        self.assertEqual(list_display, ["id", "photo", "goods", "get_html_photo"])

    def test_list_display_links(self):
        """The list display links are written correctly"""

        list_display_links = self.admin.list_display_links

        self.assertEqual(list_display_links, ["id", "photo"])

    def test_list_readonly_fields(self):
        """The list readonly fields are written correctly"""

        readonly_fields = self.admin.readonly_fields

        self.assertEqual(readonly_fields, ["get_html_photo"])

    def test_get_html_photo(self):
        """Availability of html photos"""

        picture_object = Mock()
        picture_object.photo.url = "/media/IMG_R_0067.jpg"

        html_photo = self.admin.get_html_photo(picture_object)

        self.assertEqual(html_photo, "<img src='/media/IMG_R_0067.jpg' width=50>")

    def test_dont_get_html_photo_(self):
        """Lack of html photos"""

        picture_object = Mock()
        picture_object.photo = None

        html_photo = self.admin.get_html_photo(picture_object)

        self.assertEqual(html_photo, "Без фото")
