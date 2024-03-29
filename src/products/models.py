import random
from django.db import models
import os
from django.db.models.signals import pre_save
from django.urls import reverse

from .utils import unique_slug_generator

# Create your models here.

def get_filename_ext(filename):
	base_name = os.path.basename(filename)
	name, ext = os
	path.splitname(base_name)
	return name,ext


def upload_image_path(instance,filename):
	# print(instance)
	# print(filename)	
	new_filename = random.randit(1,50000000)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)

	return "products/{new_filename}/{final_filename}".format(
		new_filename=new_filename, 
		final_filename=final_filename
		)


class ProductManager(models.Manager):
	def featured(self):
		return self.get_queryset().filter(featured= True)

	def get_by_id(self,id):
		qs =  self.get_queryset().filter(id=id)	
		if qs.count() ==1:
			return qs.first()
		return None	







class Product(models.Model):
	title 		= models.CharField(max_length=120)
	slug		= models.SlugField(blank=True, unique = True)
	description = models.TextField()
	price 		= models.DecimalField(decimal_places=2, max_digits=100, default=10.99)
	image 		= models.ImageField(upload_to = 'products/', null=True, blank=True)
	featured	= models.BooleanField(default = False)
	timestamp	= models.DateTimeField(auto_now_add = True)


	objects = ProductManager()



	def get_absolute_url(self):
		# return "/products/{slug}/".format(slug=self.slug)
		return reverse("products:detail", kwargs={"slug":self.slug})





	def __str__(self):
		return self.title 


def product_pre_save_reciever(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_reciever, sender= Product)		
