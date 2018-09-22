from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User
from .models import Category, Sub_Category, Product, Profile, Comment, Rating

class ProfileInline(admin.TabularInline):
	model = Profile

class UserAdmin(DjangoUserAdmin):
	inlines = (ProfileInline, )

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Sub_Category)
admin.site.register(Product)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Rating)