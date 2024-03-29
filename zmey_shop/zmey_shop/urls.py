"""
URL configuration for zmey_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from dotenv import load_dotenv, find_dotenv


from core import views, forms
from zmey_shop import settings

load_dotenv(find_dotenv())
handler404 = views.page_not_found
handler403 = views.page_forbidden
handler500 = views.page_server_error

admin.autodiscover()
admin.site.login_form = forms.LoginAdminUserForm
admin.site.login_template = "admin/login.html"

urlpatterns = [
    path(f'{os.getenv("ADMIN")}/', admin.site.urls),
    path("", include("goods.urls")),
    path("favourite/", include("goods_favourite.urls", namespace="favourite")),
    path("users/", include("users.urls", namespace="users")),
    path("footer/", include("footer.urls", namespace="footer")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("captcha/", include("captcha.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
