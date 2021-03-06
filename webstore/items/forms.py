from django import forms
from django.contrib.auth.models import User
from.models import Category, Sub_Category, Product, Profile
from django.contrib.auth.models import User

subs = Sub_Category.objects.all()
SUBS = (

)
counter = 1

for sub in subs:
    SUBS = SUBS + ((counter, (sub.sub_name)),)
    counter+=1

class ProductForm(forms.Form):
    class Meta:
        model = Product
        fields = ('subc', 'Product_name', 'Product_Desc', 'Price', 'Currency', 'Image')

    CURRENCIES = (
    ("USD", ("USD")),
    ("EUR", ("EUR")),
    ("GBP", ("GBP")),
    ("AUD", ("AUD")),
    ("HRK", ("HRK"))
)

    subc = forms.ChoiceField(label='Sub Category', choices = SUBS, widget = forms.Select(attrs = {'class': 'choiceclass'}))
    Product_name = forms.CharField(label='Product Name', max_length = 100, widget = forms.TextInput(attrs = {'class': 'inputstyle'}))
    Product_Desc = forms.CharField(label='Description', max_length = 10000, widget = forms.Textarea(attrs = {'class': 'textareainputstyle'}))
    Price = forms.CharField(label = 'Price', max_length = 10, widget = forms.TextInput(attrs = {'class': 'pricestyle'}))
    Currency = forms.ChoiceField(label='Currency', choices = CURRENCIES, widget = forms.Select(attrs = {'class': 'choiceclass'}))
    Image1 = forms.FileField()
    Image2 = forms.FileField(required=False)
    Image3 = forms.FileField(required=False)
    Image4 = forms.FileField(required=False)
    Image5 = forms.FileField(required=False)


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Product_name', 'Product_Desc', 'Price', 'Currency', 'Image1', 'Image2', 'Image3', 'Image4', 'Image5', ]

    CURRENCIES = (
    ("USD", ("USD")),
    ("EUR", ("EUR")),
    ("GBP", ("GBP")),
    ("AUD", ("AUD")),
    ("HRK", ("HRK"))
)

    Product_name = forms.CharField(required = False, label='Product Name', max_length = 100, widget = forms.TextInput(attrs = {'class': 'inputstyle'}))
    Product_Desc = forms.CharField(required = False, label='Description', max_length = 10000, widget = forms.Textarea(attrs = {'class': 'textareainputstyle'}))
    Price = forms.CharField(required = False, label = 'Price', max_length = 10, widget = forms.TextInput(attrs = {'class': 'pricestyle'}))
    Currency = forms.ChoiceField(required = False, label='Currency', choices = CURRENCIES, widget = forms.Select(attrs = {'class': 'choiceclass'}))
    Image1 = forms.FileField(required = False)
    Image2 = forms.FileField(required=False)
    Image3 = forms.FileField(required=False)
    Image4 = forms.FileField(required=False)
    Image5 = forms.FileField(required=False)


class LoginForm(forms.Form):
    username = forms.CharField(label = 'Username', max_length = 25, widget = forms.TextInput(attrs = {'class': 'inputstyle'}))
    password = forms.CharField(label = 'Password', max_length = 100, widget = forms.PasswordInput(attrs = {'class': 'inputstyle'}))

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
    email = forms.CharField(label = 'E-mail adress', max_length = 75, widget = forms.TextInput(attrs = {'class': 'inputstyle'}))
    username = forms.CharField(label = 'Username', max_length = 25, widget = forms.TextInput(attrs = {'class': 'inputstyle'}))
    password = forms.CharField(label = 'Password', max_length = 100, widget = forms.PasswordInput(attrs = {'class': 'inputstyle'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'city', 'adress', 'postalcode', 'first_name', 'last_name']
    city = forms.CharField(label = 'Current City  ', max_length = 100, required = False, widget = forms.TextInput(attrs = {'class': 'inputstyle'}))
    adress = forms.CharField(label = 'Home Adress ', max_length = 100, required = False, widget = forms.TextInput(attrs = {'class': 'inputstyle'}))
    postalcode = forms.DecimalField(label = 'Postal Code  ', required = False, widget = forms.TextInput(attrs = {'class': 'inputstyle'}))
    first_name = forms.CharField(label = 'First Name  ', max_length = 100, required = False, widget = forms.TextInput(attrs = {'class': 'inputstyle'}))
    last_name = forms.CharField(label = 'Last Name ', max_length = 100, required = False, widget = forms.TextInput(attrs = {'class': 'inputstyle'}))

#STILL UNUSED, WILL BE USED FOR FILTERING
class PriceRangeForm(forms.Form):
    price_range1 = forms.DecimalField(label = 'pr1')
    price_range2 = forms.DecimalField(label = 'pr2')


class UserRatingForm(forms.Form):
    rating = forms.DecimalField(label = "Rate this user!")

class CommentForm(forms.Form):
    comment_text = forms.CharField(label = 'Comment', max_length = 200, widget = forms.TextInput(attrs = {'class': 'inputstyle'}))