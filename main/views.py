from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import Category, Term, Dictionary
from .forms import DictionaryForm

# Home.
def home(request):
	'''Home.'''
	words = Dictionary.objects.all() # Get all words.
	return render(request=request, template_name='home.html', context={'words': words})

# Add word.
def add_word(request):
	'''Add word.'''
	categories = Category.objects.all()
	terms = Term.objects.all()
	if request.method == 'POST':
		form = DictionaryForm(request.POST)
		if form.is_valid():
			form.save()
			redirect(to='home')
	else:
		form = DictionaryForm()
	return render(request=request, template_name='add_word.html', context={'categories': categories, 'terms': terms, 'form': form})
