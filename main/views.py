from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import Category, Term, Dictionary

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
		en = request.POST.get('en')
		ru = request.POST.get('ru')
		uz = request.POST.get('uz')
		category_slug = request.POST.get('category')
		enpro = request.POST.get('enpro')
		rupro = request.POST.get('rupro')
		description = request.POST.get('description')
		term_slug = request.POST.get('term')
		to_process = request.POST.get('toproc', 'off') == 'on'

		category = Category.objects.get(slug=category_slug)
		term = Term.objects.get(slug=term_slug)
		
		dictionary = Dictionary(
			en=en,
			ru=ru,
			uz=uz,
			category=category,
			en_pro=enpro,
			ru_pro=rupro,
			description=description,
			term=term,
			to_process=to_process)
		dictionary.save()
		redirect(to='home')
	return render(request=request, template_name='add_word.html', context={'categories': categories, 'terms': terms})
