from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import Category, Term, Dictionary
from .forms import DictionaryForm, CategoryForm, TermForm
from django.http import HttpResponse
import pyttsx3

# Home.
def home(request):
	'''Home.'''
	words = Dictionary.objects.all() # Get all words.
	return render(request=request, template_name='home.html', context={})

# DICTIONARY.

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
        template_name='add.html',
        context={'form': form, 'name': 'Dictionary'})

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
        template_name='edit.html',
        context={'form': form, 'name': 'Dictionary'})

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
        return render(request=request, template_name='delete.html', context={'words': words})

# Details of dictionary.
def details_dictionary(request, w_id):
    '''Details of dictionary.'''
    word = Dictionary.objects.get(id=w_id)
    return render(request=request, template_name='details.html', context={'word': word})

# Speak.
def speak(request, w_id):
    '''Speak.'''
    word = Dictionary.objects.get(id=w_id)
    if word:
        engine = pyttsx3.init()
        engine.say(word.en)
        engine.runAndWait()
        return redirect(to='details_dictionary', w_id=word.id)

# Speak Russian.
def speak_ru(request, w_id):
    '''Speak Russian.'''
    word = Dictionary.objects.get(id=w_id)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    if word:
        engine.say(word.ru)
        engine.runAndWait()
        return redirect(to='details_dictionary', w_id=word.id)

# CATEGORY.

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
    return render(request=request, template_name='add.html', context={'form': form, 'name': 'Category'})

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
    return render(request=request, template_name='edit.html', context={'form': form, 'name': 'Category'})

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
        return render(request=request, template_name='delete.html', context={'categories': categories})

# TERMS.

# Add tems.
def add_term(request):
    '''Add term.'''
    if request.method == 'POST':
        form = TermForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='home')
    else:
        form = TermForm()
    return render(request=request, template_name='add.html', context={'form': form, 'name': 'Term'})

# Change term.
def change_term(request):
    '''Change term.'''
    terms = Term.objects.all() # Get all terms.
    return render(request=request, template_name='change_term.html', context={'terms': terms})

# Edit term.
def edit_term(request, t_id):
    '''Edit term.'''
    term = Term.objects.get(id=t_id)
    if request.method == 'POST':
        form = TermForm(request.POST, instance=term)
        if form.is_valid():
            form.save()
            return redirect('change_term')
    else:
        form = TermForm(instance=term)
    return render(request=request, template_name='edit.html', context={'form': form, 'name': 'Term'})

# Delete term.
def delete_term(request):
    '''Delete term.'''
    if request.method == 'POST':
        term_ids = request.POST.getlist('term_ids')
        if term_ids:
            Term.objects.filter(id__in=term_ids).delete()
        return redirect(to='home')
    else:
        terms = Term.objects.all() # Get all categories list.
        return render(request=request, template_name='delete.html', context={'terms': terms})