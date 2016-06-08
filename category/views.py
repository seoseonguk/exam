from django.shortcuts import redirect, render, get_object_or_404
from .forms import CategoryForm, ReviewForm
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

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', pk)
    else:
        form = CategoryForm(instance=category)
    context = {
        'form': form,
    }
    return render(request, "category/category_new.html", context)

def shop_detail(request, shop_pk):
    shop = get_object_or_404(Shop, pk=shop_pk)
    context = {
        'shop': shop,
    }
    return render(request, "shop/shop_detail.html", context)


def review_new(request, shop_pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = get_object_or_404(Shop, pk=shop_pk)
            review.user = request.user
            review.save()
            return redirect('shop_detail', shop_pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, "review/review_new.html", context)
def review_edit(request, shop_pk, pk):
    pass


