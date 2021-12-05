from mainapp.models import Product, Product_Category
from django import forms
from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import User


class UserAdminRegisterForm(UserRegisterForm):

    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'age', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfileForm):
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(widget=forms.TextInput())


    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['readonly'] = False
        self.fields['username'].widget.attrs['readonly'] = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class ProductAdminCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    image = forms.ImageField(widget=forms.FileInput())
    description = forms.CharField(widget=forms.TextInput())
    price = forms.DecimalField(widget=forms.NumberInput())
    quantity = forms.DecimalField(widget=forms.NumberInput())
    category = forms.ModelChoiceField(queryset=Product_Category.objects.all())


    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'quantity', 'category')

    def __init__(self, *args, **kwargs):
        super(ProductAdminCreateForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class ProductAdminProfileForm(ProductAdminCreateForm):
    pass


class CategoryAdminCreateForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Product_Category
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(CategoryAdminCreateForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class CategoryAdminProfileForm(CategoryAdminCreateForm):
    pass
