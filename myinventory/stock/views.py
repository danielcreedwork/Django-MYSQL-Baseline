from django.shortcuts import render
from .models import Type, Item
# Create your views here.

def index(request):
    """The home page for Stock."""
    return render(request, 'stock/index.html')


def types(request):
    """Show all items."""
    types = Type.objects.order_by('date_added')
    context = {'types': types}
    return render(request, 'stock/types.html', context)


def type(request, type_id):
    """Show a single topic and all its entries."""
    type = Type.objects.get(id=type_id)
    items = type.item_set.order_by('-date_added')
    context = {'type': type, 'items': items}
    return render(request, 'stock/type.html', context)
