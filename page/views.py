from django.shortcuts import render

from .models import Block, Page

def page(request, slug):
    page = Page.objects.get(slug=slug)
    context = {"blocks": page.block_set.all()}
    return render (request, "page/main.html", context)

# Create your views here.
