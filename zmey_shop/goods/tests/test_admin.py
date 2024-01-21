from unittest.mock import Mock
from django.test import TestCase
from django.contrib.admin import AdminSite

from goods.models import Goods
from goods.admin import GoodsAdmin


class AdminGoodsTest(TestCase):
    def setUp(self):
        site = AdminSite()
        model_admin = Goods
        self.admin = GoodsAdmin(model=model_admin, admin_site=site)
    
    def test_fields(self):
        """The fields are written correctly"""

        fields = self.admin.fields

        self.assertEqual(fields, ['name', 'slug', 'color', 'main_photo'])

    def test_list_display(self):
        """The list display are written correctly"""

        list_display = self.admin.list_display

        self.assertEqual(list_display, ['id', 'name', 'main_photo', 'slug', 'color', 'get_html_main_photo'])
    
    def test_list_display_links(self):
        """The list display links are written correctly"""

        list_display_links = self.admin.list_display_links

        self.assertEqual(list_display_links, ['id', 'name', 'main_photo'])
    
    def test_list_readonly_fields(self):
        """The list readonly fields are written correctly"""

        readonly_fields = self.admin.readonly_fields

        self.assertEqual(readonly_fields, ['get_html_main_photo'])
    
    def test_search_fields(self):
        """The list search fields are written correctly"""

        search_fields = self.admin.search_fields
        
        self.assertEqual(search_fields, ['name'])
    
    def test_prepopulated_fields(self):
        """The dict prepopulated fields are written correctly"""

        prepopulated_fields = self.admin.prepopulated_fields

        self.assertEqual(prepopulated_fields, {'slug': ('name',)})
    
    def test_get_html_main_photo(self):
        """Availability of html main photos"""

        picture_object = Mock()
        picture_object.main_photo.url = "/media/IMG_R_0067.jpg"

        html_photo = self.admin.get_html_main_photo(picture_object)

        self.assertEqual(html_photo, "<img src='/media/IMG_R_0067.jpg' width=50>")
    
    def test_dont_get_html_photo_(self):
        """Lack of html main photos"""

        picture_object = Mock()
        picture_object.main_photo = None

        html_photo = self.admin.get_html_main_photo(picture_object)

        self.assertEqual(html_photo, "Без фото")