from django.contrib import admin
from django.urls import path, include
from .views import add_user,list_view,delete,update,blog
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', add_user, name="add"),
    path('list_view/', list_view, name="list_view"),
    path('delete/<int:id>/', delete ,name="delete" ),
    path('update/<int:id>/', update, name="update"),
    path('blog/',blog, name="blog")
]