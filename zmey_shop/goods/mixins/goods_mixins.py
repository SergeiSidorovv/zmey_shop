from goods.models import Goods



class BaseDataMixin:
    model = Goods
    paginate_by = 15
