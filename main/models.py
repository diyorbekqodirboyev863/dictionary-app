from django.db import models
from django.utils.text import slugify

# Category.
class Category(models.Model):
	name = models.CharField(max_length=128) # Category name.
	slug = models.SlugField(max_length=128, blank=True, unique=True)
	description = models.TextField(blank=True, null=True)
	to_process = models.BooleanField(default=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name.lower())
		if self.to_process:
			self.name = self.name.title()
		super().save(*args, **kwargs)

	def __str__(self) -> str:
		return self.name

	class Meta:
		verbose_name_plural = 'Categories'

# Term.
class Term(models.Model):
	name = models.CharField(max_length=128) # Term name.
	slug = models.SlugField(max_length=128, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	to_process = models.BooleanField(default=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name.lower())
		if self.to_process:
			self.name = self.name.title()
		super().save(*args, **kwargs)

	def __str__(self) -> str:
		return self.name

# Dictionary.
class Dictionary(models.Model):
	en = models.CharField(max_length=255, verbose_name='English') # English.
	uz = models.CharField(max_length=255, verbose_name='Uzbek', blank=True, null=True) # Uzbek.
	ru = models.CharField(max_length=255, verbose_name='Russian') # Russin.
	category = models.ForeignKey(to=Category, on_delete=models.CASCADE, blank=True, null=True)
	en_pro = models.CharField(max_length=255, blank=True, null=True) # English pronunciation.
	ru_pro = models.CharField(max_length=255, blank=True, null=True) # Russin pronunciation.
	description = models.TextField(blank=True, null=True)
	term = models.ForeignKey(to=Term, on_delete=models.CASCADE, blank=True, null=True)
	to_process = models.BooleanField(default=True)

	def save(self, *args, **kwargs):
		if self.to_process:
			self.en = self.en.title()
			self.ru = self.ru.title()
			if self.uz:
				self.uz = self.uz.title()
			if self.ru_pro:
				self.ru_pro = self.ru_pro.title()
			if self.en_pro:
				self.en_pro = self.en_pro.title()
		super().save(*args, **kwargs)

	def __str__(self) -> str:
		return f'{self.en} - {self.ru} - {self.uz}'

	class Meta:
		verbose_name_plural = 'Dictionaries'
