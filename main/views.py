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
    if request.method == 'POST':
        form = DictionaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='home')
    else:
        form = DictionaryForm()

    return render(request=request,
        template_name='add_word.html',
        context={'form': form})

# Change dictionary.
def change_dict(request):
	'''Change dictionary.'''
	words = Dictionary.objects.all() # Get all words.
	return render(request=request, template_name='change_dict.html', context={'words': words})

# Edit dictionary.
def edit_dict(request, w_id):
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
        template_name='add_word.html',
        context={'form': form})

'''Delete words'''
def delete_words(request):
	if request.method == 'POST':
		word_ids = request.POST.getlist('word_ids')  # Get the list of checked word IDs.
		if word_ids:  # Check if any words were selected.
			Dictionary.objects.filter(id__in=word_ids).delete()  # Delete selected words.
		return redirect('home')  # Redirect to the home page or any other page.
	else:
		# Display the list of words.
		words = Dictionary.objects.all()
		return render(request=request, template_name='delete_words.html', context={'words': words})
