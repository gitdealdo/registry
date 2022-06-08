from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Company
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('identity_num', 'first_name', 'last_name', 'email', 'address', 'cellphone')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'user_type'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')})
    )

    list_display = (
        'username',
        'first_name',
        'last_name',
        'identity_num',
        'email',
        'is_active',
        'is_staff',
        'user_type',
    )
    list_filter = ('is_staff', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('last_name', 'email', 'first_name')
    filter_horizontal = ('groups', 'user_permissions')

admin.site.register(User, CustomUserAdmin)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'ruc', 'cellphone']
