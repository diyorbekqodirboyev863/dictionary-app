from django.urls import path
from . import views

urlpatterns = [
	path(route='', view=views.home, name='home'),
	path(route='add-dict/', view=views.add_word, name='add_word'),
	path(route='change-dict/', view=views.change_dict, name='change_dict'),
	path(route='edit-dict/<int:w_id>', view=views.edit_dict, name='edit_dict'),
	path(route='delete-words/', view=views.delete_words, name='delete_words'),
]