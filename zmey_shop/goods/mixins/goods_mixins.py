from django.core.paginator import InvalidPage
from django.http import Http404

from goods.models import Goods
from core.views import SafePaginator


class BaseDataMixin:
    """
    A basic Mixin that stores the model, the number of products on the page,
    and the pagination class for further inherited views
    """

    paginator_class = SafePaginator
    model = Goods
    paginate_by = 15

    def paginate_queryset(self, queryset, page_size):
        """
        Splits a set of queries into pages, differs from the basic function in that instead
        of an error when selecting a non-existent page, it returns either the first or
        the last page, depending on the query
        """

        paginator = self.get_paginator(
            queryset,
            page_size,
            orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty(),
        )
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
        try:
            page_number = int(page)
        except ValueError:
            if page == "last":
                page_number = paginator.num_pages
            else:
                page_number = 1
        try:
            page = paginator.page(page_number)
            return (paginator, page, page.object_list, page.has_other_pages())
        except InvalidPage as ex:
            raise Http404(ex) from ex
