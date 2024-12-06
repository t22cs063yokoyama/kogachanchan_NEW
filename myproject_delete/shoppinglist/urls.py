from django.urls import path
from .views import ItemList, ItemDeleteView, ItemAddView

app_name='shoppinglist'
urlpatterns = [
    path('list/', ItemList.as_view(),name='list'),
    path('delete', ItemDeleteView.as_view(), name='delete'),
    path("delete/id=<int:pk>",ItemDeleteView.as_view(), name='delete'), 
    path('add', ItemAddView.as_view(), name='add'),
]