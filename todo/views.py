from django.shortcuts import render,redirect
from django.contrib import messages
from .models import List
from .forms import ListForm

# Create your views here.

def home(request):
	if request.method == "POST":
		form = ListForm(request.POST or None)
		
		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request,('Item has been added to the list'))
			return render(request,'todo/index.html',{'all_items':all_items})
	else:
		all_items=List.objects.all
		return render(request,'todo/index.html',{'all_items':all_items})


def delete(request, object_id):
	item = List.objects.get(pk=object_id)
	item.delete()
	messages.success(request,('Item has been deleted from the list'))
	return redirect('home')