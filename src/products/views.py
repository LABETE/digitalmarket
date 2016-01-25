import os
from mimetypes import guess_type


from django.conf import settings
from django.core.servers.basehttp import FileWrapper
from django.db.models import Q, Avg, Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from digitalmarket.mixins import (
    AjaxRequiredMixin,
    LoginRequiredMixin,
    StaffRequiredMixin,
    SubmitBtnMixin,
    MultiSlugMixin,
)
from sellers.models import SellerAccount
from sellers.mixins import SellerAccountMixin
from analytics.models import TagView

from .forms import ProductModelForm
from .models import Product, ProductRating, MyProducts
from .mixins import ProductManagerMixin

from tags.models import Tag


class ProductRatingAjaxView(AjaxRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return JsonResponse({}, status=401)

        user = request.user
        product_id = request.POST.get("product_id")
        rating_value = request.POST.get("rating_value")
        exists = Product.objects.filter(id=product_id).exists()
        if not exists:
            return JsonResponse({}, status=404)

        try:
            product_obj = Product.objects.get(id=product_id)
        except:
            product_obj = Product.objects.filter(id=product_id).first()

        try:
            rating_obj = ProductRating.objects.get(user=user, product=product_obj)
        except ProductRating.MultipleObjectsReturned:
            rating_obj = ProductRating.objects.filter(user=user, product=product_obj).first()
        except:
            rating_obj = ProductRating()
            rating_obj.user = user
            rating_obj.product = product_obj
        rating_obj.rating = int(rating_value)
        myproducts = user.myproducts.products.all()
        if product_obj in myproducts:
            rating_obj.verified = True
        rating_obj.save()
        data = {
            "success": True
        }
        return JsonResponse(data)


class ProductCreateView(SellerAccountMixin, SubmitBtnMixin, CreateView):
    model = Product
    form_class = ProductModelForm
    template_name = "form.html"
    submit_btn = "Add Product"

    def form_valid(self, form):
        seller = self.get_account()
        form.instance.seller = seller
        valid_data = super(ProductCreateView, self).form_valid(form)
        tags = form.cleaned_data.get("tags")
        if tags:
            tags_list = tags.split(",")
            for tag in tags_list:
                if not tag == " ":
                    new_tag = Tag.objects.get_or_create(title=str(tag).strip())[0]
                    new_tag.products.add(form.instance)
        return valid_data


class ProductUpdateView(ProductManagerMixin, SubmitBtnMixin, MultiSlugMixin, UpdateView):
    model = Product
    form_class = ProductModelForm
    template_name = "form.html"
    submit_btn = "Update Product"

    def get_initial(self):
        initial = super(ProductUpdateView, self).get_initial()
        tags = self.get_object().tag_set.all()
        initial['tags'] = ", ".join([x.title for x in tags])
        return initial

    def form_valid(self, form):
        valid_data = super(ProductUpdateView, self).form_valid(form)
        tags = form.cleaned_data.get("tags")
        obj = self.get_object()
        obj.tag_set.clear()
        if tags:
            tags_list = tags.split(",")
            for tag in tags_list:
                if not tag == " ":
                    new_tag = Tag.objects.get_or_create(title=str(tag).strip())[0]
                    new_tag.products.add(self.get_object())
        return valid_data


class SellerProductListView(SellerAccountMixin, ListView):
    model = Product
    template_name = "sellers/product_list_view.html"

    def get_queryset(self, *args, **kwargs):
        qs = super(SellerProductListView, self).get_queryset(*args, **kwargs)
        qs = qs.filter(seller=self.get_account())
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                        Q(title__icontains=query) |
                        Q(description__icontains=query)
                ).order_by("title")
        return qs


class VendorListView(ListView):
    model = Product
    template_name = "products/product_list.html"

    def get_object(self):
        username = self.kwargs.get("vendor_name")
        seller = get_object_or_404(SellerAccount, user__username=username)
        return seller

    def get_context_data(self, *args, **kwargs):
        context = super(VendorListView, self).get_context_data(*args, **kwargs)
        context["vendor_name"] = str(self.get_object().user.username)
        return context

    def get_queryset(self, *args, **kwargs):
        seller = self.get_object()
        qs = super(VendorListView, self).get_queryset(*args, **kwargs).filter(seller=seller)
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                        Q(title__icontains=query) |
                        Q(description__icontains=query)
                ).order_by("title")
        return qs


class ProductListView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                        Q(title__icontains=query) |
                        Q(description__icontains=query)
                ).order_by("title")
        return qs


class UserLibraryListView(LoginRequiredMixin, ListView):
    model = MyProducts
    template_name = "products/library_list.html"

    def get_queryset(self, *args, **kwargs):
        obj = MyProducts.objects.get_or_create(user=self.request.user)[0]
        qs = obj.products.all()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                        Q(title__icontains=query) |
                        Q(description__icontains=query)
                ).order_by("title")
        return qs


class ProductDetailView(MultiSlugMixin, DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        obj = self.get_object()
        tags = obj.tag_set.all()
        rating_avg = obj.productrating_set.aggregate(Avg("rating"), Count("rating"))
        context['rating_avg'] = rating_avg
        if self.request.user.is_authenticated():
            rating_obj = ProductRating.objects.filter(user=self.request.user, product=obj)
            if rating_obj.exists():
                context["my_rating"] = rating_obj.first().rating
            for tag in tags:
                TagView.objects.add_count(self.request.user, tag)
        return context

class ProductDownloadView(MultiSlugMixin, DetailView):
    model = Product

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj in request.user.myproducts.products.all():
            filepath = os.path.join(settings.PROTECTED_ROOT, obj.media.path)
            guessed_type = guess_type(filepath)[0]
            wrapper = FileWrapper(open(filepath, "rb"))
            mimetype = 'application/force-download'
            if guessed_type:
                mimetype = guessed_type
            response = HttpResponse(wrapper, content_type=mimetype)

            if not request.GET.get("preview"):
                response[
                    "Content-Disposition"] = "attachment; filename={0}".format(obj.media.name)

            response["X-SendFile"] = str(obj.media.name)
            return response


