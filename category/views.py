from django.shortcuts import render, get_object_or_404
from .models import Category, Shop



def index(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
    }
    return render(request, "category/index.html", context)

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    context = {
        'category': category,
    }
    return render(request, "category/category_detail.html", context)