from django.shortcuts import render
from django.views.generic import ListView
from .models import Item, Shop
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from .forms import ItemBuy, ItemIdForm, ItemForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView

# Create your views here.

class ItemList(ListView):
    model = Item
    
    def post(self, request, *args, **kwargs):
        item_id = self.request.POST.get('item_id')
        item = get_object_or_404(Item, pk=item_id)
        item_status = self.request.POST.get('item_status')
        item.buy = item_status
        item.save()
        return HttpResponseRedirect(
            reverse('shoppinglist:list'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ItemBuy()
        return context

class ItemDeleteView(UpdateView):
   model = Item
   template_name = 'shoppinglist/item_delete.html'
   success_url = 'list/'
   fields=[]

   def post(self, request, *args, **kwargs):
        item_id = self.kwargs.get('pk')
        item = self.request.POST.get('item_id')
        item = get_object_or_404(Item, pk=item_id)
        item.delete()
        
        return HttpResponseRedirect(reverse('shoppinglist:list'))
    
class ItemAddView(CreateView):
    model = Item
    fields = ('name', 'item_url', 'count', 'buy_date', 'shop')
    template_name = 'shoppinglist/item_add.html'
    success_url = 'list/'