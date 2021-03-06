from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from.models import Category, Sub_Category, Product, Profile, Comment, Rating
from.forms import ProductForm, LoginForm, RegistrationForm, PriceRangeForm, ProfileForm, ProductEditForm, UserRatingForm, CommentForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from webstore.settings import *
from django import forms
import os


def login(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You cannot login or register since you already are logged in")
    else:
        user = None
    all_categories = Category.objects.all()

    #user registration
    if request.method == 'POST' and 'regbtn' in request.POST:
        reg_form = RegistrationForm(request.POST)
        login_form = LoginForm(request.POST)
        if reg_form.is_valid():

            user = reg_form.save(commit = False)
            email = reg_form.cleaned_data['email']
            username = reg_form.cleaned_data['username']
            if User.objects.filter(username = username).exists():
                raise forms.ValidationError(_("This username already exists!"))
            password = reg_form.cleaned_data['password']

            # user.set_password(password) #this is the only way to change a password because of hashing
            user.set_password(password)
            user.save()

            user = authenticate(username = username, password = password)
            return redirect('/items/')

    #user login
    elif request.method == 'POST' and 'loginbtn' in request.POST:
        login_form = LoginForm(request.POST)
        reg_form = RegistrationForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
        

        #returns the User obejects if credintials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('/items/')
            else:
                raise forms.ValidationError(("Invalid credintials! Please, try again!"))
    else:
        reg_form = RegistrationForm()
        login_form = LoginForm()

    return render(request, 'login.html', {'login_form': login_form, 'reg_form': reg_form})


def logout(request):
    user = request.user
    if user.is_authenticated:
        auth_logout(request)
    return redirect('/items/')


def my_profile(request):
    user = request.user
    if user.is_authenticated:
        profile = request.user.profile
        products_list = []
        try:
            for product in Product.objects.filter(user = user):
                products_list.append(product)
        except(KeyError, Product.DoesNotExist):
            products = None
        if request.method == 'POST' and 'update' in request.POST:
            profile_form = ProfileForm(request.POST)
            if profile_form.is_valid():
                if profile_form.cleaned_data['city'] != '':
                    user.profile.city = profile_form.cleaned_data['city']
                else:
                    user.profile.city = user.profile.city
                if profile_form.cleaned_data['adress'] != '':
                    user.profile.adress = profile_form.cleaned_data['adress']
                else:
                    user.profile.adress = user.profile.adress
                if profile_form.cleaned_data['postalcode'] != None:
                    user.profile.postalcode = profile_form.cleaned_data['postalcode']
                else:
                    user.profile.postalcode = user.profile.postalcode
                if profile_form.cleaned_data['first_name'] != '':
                    user.first_name = profile_form.cleaned_data['first_name']
                else:
                    user.first_name = user.first_name
                if profile_form.cleaned_data['last_name'] != '':
                    user.last_name = profile_form.cleaned_data['last_name']
                else:
                    user.last_name = user.last_name 
                user.profile.user_id = user.profile.user_id
                user.profile.save()
                user.save()
        else:
            profile_form = ProfileForm()

        return render(request, 'my_profile.html', {'user': user, 'profile': profile, 'profile_form': profile_form, 'products_list': products_list})
    else:
        return HttpResponse("You can't access this page because you are not logged in!")

def userprofile(request, username):
    user = request.user
    requested_user = get_object_or_404(User, username = username)
    if requested_user == user:
        return redirect('/items/my_profile/') 
    products_list = []
    try:
        for product in Product.objects.filter(user = requested_user):
            products_list.append(product)
    except(KeyError, Product.DoesNotExist):
        products = None

    if user.is_authenticated:
        if request.method == 'POST':
            rating_form = UserRatingForm(request.POST)
            if rating_form.is_valid():
                if Rating.objects.filter(rated_user = requested_user, reviewer = user):
                    return HttpResponse("You cannot rate the same user twice!")
                else:
                    if rating_form.cleaned_data['rating'] > 5:
                        return HttpResponse("The rating you give to the user cannot be greater than five!")
                    else:
                        rating = Rating()
                        rating.rated_user = requested_user
                        rating.reviewer = user
                        rating.rating = rating_form.cleaned_data['rating']
                        requested_user.profile.total_rating += rating.rating
                        requested_user.profile.number_of_ratings += 1
                        requested_user.profile.avg_rating = requested_user.profile.total_rating/requested_user.profile.number_of_ratings
                        requested_user.profile.save()
                        user.profile.save()
                        rating.save()
                        return redirect(f"/items/users/{username}/")
        else:
            rating_form = UserRatingForm()

        if not products_list:
            return HttpResponse('This user cannot be rated since he/she has not posted any products yet!')


    return render(request, 'user_profile.html', {'user': user, 'requested_user': requested_user, 'products_list': products_list, 'rating_form': rating_form})

def index(request):
    user = request.user
    all_categories = Category.objects.all()

    return render(request, 'index.html', {'all_categories': all_categories, 'user': user})

def subs(request, category_name):
    category = get_object_or_404(Category, category_name = category_name)
    return render(request, 'subs.html', {'category': category})

def products(request, category_name, sub_name):
    category = get_object_or_404(Category, category_name = category_name)
    sub_category = get_object_or_404(Sub_Category, sub_name = sub_name)
    return render(request, 'products.html', {'sub_category': sub_category, 'category': category})

def product_detail(request, category_name, sub_name, product_name):
    product = get_object_or_404(Product, product_name = product_name)
    user = request.user
    if request.method == 'POST' and 'delete' in request.POST:
        if user == product.user:
            os.chdir("..")
            os.remove(f'webstoremedia/{product.image1}')
            try:
                os.remove(f'webstoremedia/{product.image2}')
            except:
                pass

            try:
                os.remove(f'webstoremedia/{product.image3}')
            except:
                pass

            try:
                os.remove(f'webstoremedia/{product.image4}')
            except:
                pass

            try:
                os.remove(f'webstoremedia/{product.image5}')
            except:
                pass

            product.delete()
            return redirect('/items/my_profile/')
        else:
            return HttpResponse("You cannot delete a product because you are not the user who created the product!")

    elif request.method == 'POST' and 'edit' in request.POST:
        if user == product.user:
            return redirect(f'/items/edit_a_product/{product.product_name}')
        else:
            return HttpResponse("You cannot edit product information because you are not the user who created the product!")

    if request.method == 'POST' and 'comment' in request.POST:
        comment_form = CommentForm(request.POST)
        if user.is_authenticated:
            if user != product.user:
                if comment_form.is_valid():
                    if not Comment.objects.filter(user = user, product = product):
                        comment = Comment()
                        comment.user = user
                        comment.product = product
                        comment.comment_text = comment_form.cleaned_data['comment_text']
                        comment.save()
                        return redirect(f"/items/{category_name}/{sub_name}/{product_name}/")
                    else:
                        return HttpResponse("You cannot comment on the same product twice. We are sorry, but this is to prevent spamming!")
            else:
                return HttpResponse('You cannot comment your own product!')
        else:
             return HttpResponse('You cannot comment because you are not logged in!')       

    else:
        comment_form = CommentForm()

    return render(request, 'product_detail.html', {'product': product, 'category_name': category_name, 'user': user, 'comment_form': comment_form})



def add_a_product(request):
    global MEDIA_ROOT
    all_categories = Category.objects.all()
    all_subs = Sub_Category.objects.all()
    user = request.user

    if user.is_authenticated:
        if user.first_name and user.last_name and user.profile.city and user.profile.adress and user.profile.postalcode:
            if request.method == 'POST':
                form = ProductForm(request.POST, request.FILES)
                if form.is_valid():
                    selected_sub = Sub_Category.objects.get(pk = form.cleaned_data['subc'])
                    seller = User.objects.get(username = user.username)
                    product = Product()
                    product.sub = selected_sub
                    product.user =  seller
                    product.product_name = form.cleaned_data['Product_name']
                    if Product.objects.filter(product_name = product.product_name):
                        return HttpResponse("There is a product with the exact same name, please name your product diffrently!")
                    product.product_desc = form.cleaned_data['Product_Desc']
                    product.product_price_value = form.cleaned_data['Price']
                    product.product_price_currency = form.cleaned_data['Currency']

                    product.image1 = form.cleaned_data['Image1']

                    if form.cleaned_data['Image2'] is not None:
                        product.image2 = form.cleaned_data['Image2']
                    if form.cleaned_data['Image3'] is not None:
                        product.image3 = form.cleaned_data['Image3']
                    if form.cleaned_data['Image4'] is not None:
                        product.image4 = form.cleaned_data['Image4']
                    if form.cleaned_data['Image5'] is not None:
                        product.image5 = form.cleaned_data['Image']
                    product.save()
                    return redirect('/items/')
            else:
                form = ProductForm()
        else:
            return HttpResponse("You have to fill out your additional user information before posting any products!")
    else:
        return HttpResponse('You cannot add products since you are not logged in!')

    passes = {

        'all_categories': all_categories,
        'all_subs': all_subs,
        'form': form,
        'MEDIA_ROOT': MEDIA_ROOT

    }
    return render(request, 'add_a_product.html',  passes)

def about(request):
    user = request.user
    return render(request, 'about.html', {'user': user})

def edit_a_product(request, product_name):
    user = request.user
    product = get_object_or_404(Product, product_name = product_name)
    if product.user == user:
        if request.method == 'POST':
            form = ProductEditForm(request.POST, instance = product)
            if form.is_valid():
                product.sub = product.sub
                product.user = user

                if form.cleaned_data['Product_name'] != '':
                    product.product_name = form.cleaned_data['Product_name']
                else:
                    product.product_name = product.product_name 

                if form.cleaned_data['Product_Desc'] != '':
                    product.product_desc = form.cleaned_data['Product_Desc']
                else:
                    product.product_desc = product.product_desc

                if form.cleaned_data['Price'] != '':
                    product.product_price_value = form.cleaned_data['Price']
                else:
                    product.product_price_value = product.product_price_value

                product.product_price_currency = form.cleaned_data['Currency']

                if form.cleaned_data['Image1'] is not None:
                    product.image1 = form.cleaned_data['Image1']

                if form.cleaned_data['Image2'] is not None:
                    product.image2 = form.cleaned_data['Image2']
                if form.cleaned_data['Image3'] is not None:
                    product.image3 = form.cleaned_data['Image3']
                if form.cleaned_data['Image4'] is not None:
                    product.image4 = form.cleaned_data['Image4']
                if form.cleaned_data['Image5'] is not None:
                    product.image5 = form.cleaned_data['Image']

                product.save()
                return redirect('/items/')

        else:
            form = ProductEditForm()

    return render(request, 'edit_a_product.html', {'form': form, 'product': product, 'user': user})


