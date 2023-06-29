from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email','role']
    fieldsets = (
        (('User'), {'fields': ('username','personal_id','first_name','last_name','email','password','department','base','country','mission','role')}),
    )

    add_fieldsets =(
        (('User'), {'fields': ('username','personal_id','first_name','last_name','email','password1','password2','department','base','country','mission','role')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Request)
admin.site.register(FileCode)
admin.site.register(FinalPapers)