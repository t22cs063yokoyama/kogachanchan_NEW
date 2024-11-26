from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Friend
from django.views.generic import ListView, DetailView

class FriendList(ListView):
    model = Friend
    
class FriendDetail(DetailView):
    model = Friend