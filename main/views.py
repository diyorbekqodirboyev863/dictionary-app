from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import Category, Term, Dictionary
from .forms import DictionaryForm, CategoryForm

# Home.
def home(request):
	'''Home.'''
	words = Dictionary.objects.all() # Get all words.
	return render(request=request, template_name='home.html', context={})

# Add dictionary.
def add_dictionary(request):
    '''Add dictionary.'''
    if request.method == 'POST':
        form = DictionaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='home')
    else:
        form = DictionaryForm()

    return render(request=request,
        template_name='add_dictionary.html',
        context={'form': form})

# Change dictionary.
def change_dictionary(request):
	'''Change dictionary.'''
	words = Dictionary.objects.all() # Get all words.
	return render(request=request, template_name='change_dictionary.html', context={'words': words})

# Edit dictionary.
def edit_dictionary(request, w_id):
    '''Edit dictionary.'''
    word = Dictionary.objects.get(id=w_id)
    if request.method == 'POST':
        form = DictionaryForm(request.POST, instance=word)
        if form.is_valid():
            form.save()
            return redirect(to='home')
    else:
        form = DictionaryForm(instance=word)

    return render(request=request,
        template_name='edit_dictionary.html',
        context={'form': form})

# Delete dictionary.
def delete_dictionary(request):
    '''Delete dictionary.'''
    if request.method == 'POST':
        word_ids = request.POST.getlist('word_ids')
        if word_ids:
            Dictionary.objects.filter(id__in=word_ids).delete()
        return redirect(to='home')
    else:
        # Display the list of words.
        words = Dictionary.objects.all()
        return render(request=request, template_name='delete_dictionary.html', context={'words': words})

# Add category.
def add_category(request):
    '''Add category.'''
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='home')
    else:
        form = CategoryForm()
    return render(request=request, template_name='add_category.html', context={'form': form})

# Chane category.
def change_category(request):
    '''Change category.'''
    categories = Category.objects.all() # Get all categories.
    return render(request=request, template_name='change_category.html', context={'categories': categories})

# Edit category.
def edit_category(request, c_id):
    '''Edit category.'''
    category = Category.objects.get(id=c_id) # Get current category id.
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect(to='change_category')
    else:
        form = CategoryForm(instance=category)
    return render(request=request, template_name='edit_category.html', context={'form': form})

# Delete category.
def delete_category(request):
    '''Delete category.'''
    if request.method == 'POST':
        category_ids = request.POST.getlist('category_ids')
        if category_ids:
            Category.objects.filter(id__in=category_ids).delete()
        return redirect(to='home')
    else:
        categories = Category.objects.all() # Get all categories list.
        return render(request=request, template_name='delete_category.html', context={'categories': categories})