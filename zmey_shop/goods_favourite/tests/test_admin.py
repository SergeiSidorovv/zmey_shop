from django.test import TestCase
from django.contrib.admin import AdminSite

from goods_favourite.models import Favourite
from goods_favourite.admin import FavouriteAdmin


class FavouriteAdminTest(TestCase):
    def setUp(self):
        site = AdminSite()
        model_admin = Favourite
        self.admin = FavouriteAdmin(model=model_admin, admin_site=site)

    def test_fields(self):
        """The fields are written correctly"""

        fields = self.admin.fields

        self.assertEqual(fields, ["user", "goods"])

    def test_list_display(self):
        """The list display are written correctly"""

        list_display = self.admin.list_display

        self.assertEqual(list_display, ["id", "user", "goods"])

    def test_search_fields(self):
        """The list search fields are written correctly"""

        search_fields = self.admin.search_fields

        self.assertEqual(search_fields, ["id"])
