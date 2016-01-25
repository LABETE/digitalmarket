from django.shortcuts import render

# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from analytics.models import TagView

from .models import Tag


class TagDetailView(DetailView):
    model = Tag

    def get_context_data(self, *args, **kwargs):
        context = super(TagDetailView, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated():
            TagView.objects.add_count(self.request.user, self.get_object())
        return context


class TagListView(ListView):
    model = Tag

    def get_queryset(self):
        return Tag.objects.all()