from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.


# function-based view
def index(request):
    item_list = Item.objects.all()

    context={
        'item_list': item_list,
    }
    return render(request, 'sizzleslice/index.html', context)

class IndexClassView(ListView):
    model = Item
    template_name = 'sizzleslice/index.html'
    context_object_name = 'item_list'


def item(request):
    return HttpResponse('<h1> this is an item</h1>')


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)

    context={
        'item': item,
    }
    return render(request, 'sizzleslice/detail.html', context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'sizzleslice/detail.html'

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('sizzleslice:index')

    return render(request, 'sizzleslice/item-form.html', {'form':form})
# class based view for add item


class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_intro', 'item_image']
    template_name = 'sizzleslice/item-form.html'

    def form_valid(self, form):
        form.instance.user_name= self.request.user

        return super().form_valid(form)


def edit_item(request,id):
    item= Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('sizzleslice:index')

    return render(request, 'sizzleslice/item-form.html', {'form':form, 'item':item})

def delete_item(request,id):
    item= Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('sizzleslice:index')

    return render(request, 'sizzleslice/item-delete.html', {'item': item})
