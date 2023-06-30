from django.shortcuts import render
from shop.models import Item, Category


# Create your views here.
def item(request):
    list = Item.objects.all()
    return render(request, 'shop.html', {"items": list})
