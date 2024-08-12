from django.contrib import admin
from .models import Category, Term, Dictionary

# Category.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug',)
	prepopulated_fields = {'slug': ('name',)}

# Terms.
@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug',)
	prepopulated_fields = {'slug': ('name',)}

# Dictionary.
@admin.register(Dictionary)
class DictionaryAdmin(admin.ModelAdmin):
	list_display = ('en', 'uz', 'ru', 'category',)
	list_filter = ('category',)