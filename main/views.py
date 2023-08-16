from django.shortcuts import render,get_object_or_404
from django.views import View
from productsapp.models import Product,Category
from usersapp.models import Saved

# Create your views here.

def for_all_pages(request):
    if request.user.is_authenticated:
        saveds_count = Saved.objects.filter(author=request.user)
    else:
        saveds_count = 0
    categories = Category.objects.all()
    if not 'recently_viewed' in request.session:
        products_viewed_count = []
    else:
        r_viewed = request.session['recently_viewed']
        products_viewed_count = Product.objects.filter(id__in = r_viewed)
    return {'categories':categories,'products_viewed_count':products_viewed_count,'saveds_count':saveds_count}

class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        q = request.GET.get('q','')
        if q:
            products = products.filter(title__icontains=q)
        return render(request, 'index.html', {'products':products})
    
class CategoryView(View):
    def get(self, request,category_name):
        category = get_object_or_404(Category,name=category_name)
        products = Product.objects.filter(category=category)
        q = request.GET.get('q','')
        if q:
            products = products.filter(title__icontains=q)
        return render(request, 'category.html', {'products':products,'category':category})
    
