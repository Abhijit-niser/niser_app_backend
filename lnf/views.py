# from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .forms import *
from .models import *

# Create your views here.

def all_items(request):
    items = Item.objects.filter(claimed = False)
    return render(request, 'lnf/index.html', {'kind': 'Recently Added', 'items': items})

def lost_items(request):
    items = Item.objects.filter(kind = 'Lost', claimed = False)
    return render(request, 'lnf/index.html', {'kind': 'Lost', 'items': items})

def found_items(request):
    items = Item.objects.filter(kind = 'Found', claimed = False)
    return render(request, 'lnf/index.html', {'kind': 'Found', 'items': items})

class ItemDetail(DetailView):
    model = Item
    template_name = 'lnf/item.html'

def submit_view(request):
    form = ItemForm
    return render(request, 'lnf/submit.html', {'form': form})

# def search(request):
#     if request.method == 'GET':
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             search_string = form.cleaned_data['keyword']

#             words = search_string.lower().split(' ')

#             vector = SearchVector('kind', 'location', 'category',
#                         'desc', 'submitter')

#             query = SearchQuery(words[0])
#             for word in words[1:]:
#                 query = query | SearchQuery(word)

#             items = Item.objects.annotate(rank=SearchRank(vector,
#                 query)).order_by('-rank')

#             return render(request, 'lnf/search.html',
#                     {'search_string': search_string, 'items': items})

#     return HttpResponseRedirect('/')
