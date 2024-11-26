from django.contrib import admin
from django.urls import path
from friend import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('list/', views.FriendList.as_view(), name="list"),
    path('<int:pk>/', views.FriendDetail.as_view(), name="detail"),
]
