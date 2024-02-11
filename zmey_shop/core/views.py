import logging
from django.shortcuts import render
from django.core.paginator import Paginator


logger = logging.getLogger("django")


def page_not_found(request, exception):
    """Returns information about the 404 error for the page template"""

    return render(request, "404.html", status=404)


def page_forbidden(request, exception):
    """Returns information about the 403 error for the page template"""

    return render(request, "403.html", status=403)


def page_server_error(request):
    """Returns information about the 500 error for the page template"""

    return render(request, "500.html", status=500)


class SafePaginator(Paginator):
    """Checks the url request for the correctness of the requested pagination"""

    def validate_number(self, number) -> int:
        """
        Checks the transmitted page number for the possibility of an error and
        returns either the corrected version or the requested one
        """

        try:
            if isinstance(number, float) and not number.is_integer():
                number = 1
            number = int(number)
        except (TypeError, ValueError):
            number = 1
        if number <= 0:
            number = 1

        return min(number, self.num_pages)
