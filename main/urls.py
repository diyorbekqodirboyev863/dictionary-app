from django.urls import path
from . import views

urlpatterns = [
	path(route='', view=views.home, name='home'),

	# Dictionary.
	path(route='add/dictionary/', view=views.add_dictionary, name='add_dictionary'),
	path(route='change/dictionary/', view=views.change_dictionary, name='change_dictionary'),
	path(route='edit/dictionary/<int:w_id>/', view=views.edit_dictionary, name='edit_dictionary'),
	path(route='delete/dictionary/', view=views.delete_dictionary, name='delete_dictionary'),

	# Category.
	path(route='add/category/', view=views.add_category, name='add_category'),
	path(route='change/category/', view=views.change_category, name='change_category'),
	path(route='edit/category/<int:c_id>/', view=views.edit_category, name='edit_category'),
	path(route='delete/category/', view=views.delete_category, name='delete_category'),
]