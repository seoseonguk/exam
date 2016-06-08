from django.shortcuts import redirect, render, get_object_or_404
from .forms import CategoryForm
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

def category_new(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, "category/category_new.html", context)