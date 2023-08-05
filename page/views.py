from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse
from django.urls import reverse

from .models import Block, Page

def page(request, slug):
    page = Page.objects.get(slug=slug)
    context = {"blocks": page.block_set.all().order_by('order'),
               "page": page}
    return render (request, "page/main.html", context)


def download_page(request, slug):
    page = Page.objects.get(slug=slug)
    context = {"blocks": page.block_set.all().order_by('order'),
               "page": page}
    page_content = render (request, "page/main.html", context)
    
    response = HttpResponse(page_content, content_type='text/html')
    response['Content-Disposition'] = 'attachment; filename="pagina-acessivel.html"'

    return response
    
