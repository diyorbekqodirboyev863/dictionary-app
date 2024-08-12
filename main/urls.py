from django.urls import path
from . import views

urlpatterns = [
	path(route='', view=views.home, name='home'),
	path(route='add/word/', view=views.add_word, name='add_word'),
]