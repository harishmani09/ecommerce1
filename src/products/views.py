from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import Http404
from .models import Product




class ProductFeaturedListView(ListView):
	# queryset = Product.objects.all()
	template_name = "products/list.html"

	def get_queryset(self, *args, **kwargs):
		request= self.request
		return Product.objects.featured()



class ProductFeaturedDetailView(DetailView):
	# queryset = Product.objects.all()
	template_name = "products/featured-detail.html"

	def get_queryset(self, *args, **kwargs):
		request= self.request
		return Product.objects.featured()



class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"

	def get_queryset(self, *args , **kwargs):
		request = self.request
		return Product.objects.all()



def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		"qs": queryset
	}	
	return render(request, "products/list.html", context)		



class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"


	def get_object(self, *args, **kwargs):
		request = self.request
		slug = self.kwargs.get('slug')	

		# instance = get_object_or_404(Product, slug=slug)
		try:
			instance = Product.objects.get(slug=slug)
		except Product.DoesNotExist:
			raise Http404("Not Found")
		except Product.MultipleObjectsReturned:
			qs = Product.objects.filter(slug=slug)		
			instance = qs.first()
		except: 
			raise Http404("ohhh")
		return instance		


class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"


	def get_object(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')	

		instance = Product.objects.get_by_id(pk)
		if instance is None:
			raise Http404("product doesnt exists")
		return instance
	# def get_queryset(self, *args, **kwargs):
	# 	request = self.request
	# 	pk = self.kwargs.get('pk')
	# 	return Product.objects.filter(pk=pk)

def product_detail_view(request, pk=None, *args, **kwargs):
	
	instance = Product.objects.get_by_id(pk)
	if instance is None:
		raise Http404("product doesn't exist")

	print(instance)
	qs = Product.objects.filter(id=pk)
	# print(qs)
	if qs.exists() and qs.count() ==1:
		instance = qs.first()
	else:
		raise Http404("product doesn't exist")		


	context = {
		"object": instance
	}	
	return render(request, "products/detail.html", context)		
