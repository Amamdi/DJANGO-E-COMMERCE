from django.shortcuts import render
from .models import item


def item_list(request):
    context = {
        'items': item.objects.all()
    }

    return render(request, 'home-page.html', context)
