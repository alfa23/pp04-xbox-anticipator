from django.contrib import admin
'''
Custom User Model process referenced from:
https://testdriven.io/blog/django-custom-user-model/
'''
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Game, Rating, Comment


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        'email', 'first_name', 'last_name', 'date_joined',
        'is_staff', 'is_active')
    list_filter = ('email', 'first_name', 'last_name',)
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'first_name', 'last_name')
            }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)


# Xbox Anticipator code - admin:


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    '''Register Game model to admin panel'''
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'game_info', 'release_date']
    list_display = ('title', 'slug', 'status', 'release_date', 'created_date')
    list_filter = ('status', 'release_date', 'created_date', 'dev_pub')
    actions = ['publish_draft']

    def publish_draft(self, request, queryset):
        queryset.update(status=1)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    '''Register Rating model to admin panel'''
    search_fields = ['game', 'rate', 'user']
    list_display = ('game', 'rate', 'user')
    list_filter = ('game', 'rate', 'user')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Register Comment model to admin panel'''
    search_fields = ['game', 'content', 'user']
    list_display = ('game', 'content', 'posted_on', 'user', 'approved')
    list_filter = ('game', 'posted_on', 'approved')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
