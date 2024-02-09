import logging
from django.shortcuts import render
from django.core.paginator import Paginator


logger = logging.getLogger("django")


def page_not_found(request, exception):
    return render(request, "404.html", status=404)


def page_forbidden(request, exception):
    return render(request, "403.html", status=403)


def page_server_error(request):
    return render(request, "500.html", status=500)


class SafePaginator(Paginator):
    def validate_number(self, number):
        try:
            if isinstance(number, float) and not number.is_integer():
                number = 1
            number = int(number)
        except (TypeError, ValueError):
            number = 1
        if number <= 0:
            number = 1
        return min(number, self.num_pages)
