from django.http import Http404

from sellers.mixins import SellerAccountMixin


class ProductManagerMixin(SellerAccountMixin):
    def get_object(self, *args, **kwargs):
        seller = self.get_account()
        obj = super(ProductManagerMixin, self).get_object(*args, **kwargs)
        if obj.seller == seller:
            return obj
        else:
            raise Http404