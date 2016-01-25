import datetime
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import View

from django.shortcuts import render

from products.models import Product, MyProducts

from digitalmarket.mixins import AjaxRequiredMixin

from billing.models import Transaction


class CheckoutAjaxView(AjaxRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return JsonResponse({}, status=401)

        user = request.user
        product_id = request.POST.get("product_id")
        exists = Product.objects.filter(id=product_id)
        if not exists:
            return JsonResponse({}, status=404)

        try:
            product_obj = Product.objects.get(id=product_id)
        except:
            product_obj = Product.objects.filter(id=product_id).first()

        transaction_obj = Transaction.objects.create(user=request.user,
            product=product_obj,
            price=product_obj.get_price)
        my_products = MyProducts.objects.get_or_create(user=user)[0]
        my_products.products.add(product_obj)
        download_link = product_obj.get_download()
        preview_link = download_link + "?preview=True"
        data = {
            "download": download_link,
            "preview": preview_link
        }
        return JsonResponse(data)


# class CheckoutView(View):

#     def post(self, request, *args, **kwargs):
#         if request.is_ajax():
#             if not request.user.is_authenticated():
#                 data = {
#                     "works": False
#                 }
#                 return JsonResponse(data, status=401)
#             data = {
#                 "works": True,
#                 "time": datetime.datetime.now()
#             }
#             return JsonResponse(data)
#         return HttpResponse("hello")


#     def get(self, request, *args, **kwargs):
#         context = {}
#         return render(request, "checkout/test.html", context)
