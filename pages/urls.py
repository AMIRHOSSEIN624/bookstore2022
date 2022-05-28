from django.urls import path
from .views import HomeView, detail_page, search_bar, favorite_book, favorite_list

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/detail/', detail_page, name='detail_page'),
    path('search/', search_bar, name='search'),
    path('<int:pk>/favorite/', favorite_book, name='favorite_book'),
    path('favorite/list/', favorite_list, name='favorite_list'),

]
