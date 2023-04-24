from . import views
from django.urls import path

app_name = 'quotes_site'
urlpatterns = [
    path("", views.index, name="index"),
    path('<int:id>/', views.author_details, name='author_details'),
    path('add_author', views.add_author, name="add_author"),
    path('add_quote', views.add_quote, name="add_quote")
]