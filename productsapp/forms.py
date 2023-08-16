from productsapp.models import Product

from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.attrs['multiple'] = True


class NewProductForm(forms.ModelForm):
    images = forms.ImageField(widget=MultipleFileInput(), required=False)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'address', 'category', 'phone_number', 'tg_username']

    def save(self, request, commit=True):
        product = self.instance
        product.author = request.user
        super().save(commit)
        return product


class ProductForm(forms.ModelForm):
    images = forms.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'address', 'category', 'phone_number', 'tg_username']
