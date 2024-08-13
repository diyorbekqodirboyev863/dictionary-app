from django.urls import path
from . import views

urlpatterns = [
	path(route='', view=views.home, name='home'),

	# Dictionary.
	path(route='add/dictionary/', view=views.add_dictionary, name='add_dictionary'),
	path(route='change/dictionary/', view=views.change_dictionary, name='change_dictionary'),
	path(route='edit/dictionary/<int:w_id>/', view=views.edit_dictionary, name='edit_dictionary'),
	path(route='delete/dictionary/', view=views.delete_dictionary, name='delete_dictionary'),
	path(route='details/dictionary/<int:w_id>/', view=views.details_dictionary, name='details_dictionary'),
	# Speak.
	path(route='speak/<int:w_id>/', view=views.speak, name='speak'),
	path(route='speak/ru/<int:w_id>/', view=views.speak_ru, name='speak_ru'),

	# Category.
	path(route='add/category/', view=views.add_category, name='add_category'),
	path(route='change/category/', view=views.change_category, name='change_category'),
	path(route='edit/category/<int:c_id>/', view=views.edit_category, name='edit_category'),
	path(route='delete/category/', view=views.delete_category, name='delete_category'),

	# Term.
	path(route='add/term/', view=views.add_term, name='add_term'),
	path(route='change/term/', view=views.change_term, name='change_term'),
	path(route='edit/term/<int:t_id>', view=views.edit_term, name='edit_term'),
	path(route='delete/term/', view=views.delete_term, name='delete_term'),
]