from django.urls import path
from .views import *

urlpatterns = [
    path('category/list/', CategoriesList.as_view(), name='categories_list'),
    path('category/<int:pk>/book/list/', CategoryBooks.as_view(), name='category_books'),

    path('category/<int:pk>/subcategory/list/', SubategoriesList.as_view(), name='subcategories_list'),
    path('subcategory/<int:pk>/book/list/', SubategoryBooks.as_view(), name='subcategory_books'),

    path('book/list/', BooksList.as_view(), name='books_list'),
    path('book/create/', BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/detail/', BookDetail.as_view(), name='book_detail'),
    path('book/<int:pk>/edit/', BookEdit.as_view(), name='book_edit'),
    path('book/<int:pk>/delete/', BookDelete.as_view(), name='book_delete'),

    path('review/create/', ReviewCreate.as_view(), name='review_create'),
    path('review/<int:pk>/detail/', ReviewDetail.as_view(), name='review_detail'),
    path('review/<int:pk>/edit/', ReviewEdit.as_view(), name='review_edit'),
    path('review/<int:pk>/delete/', ReviewDelete.as_view(), name='review_delete'),

    path('favorite/list/', FavoriteList.as_view(), name='favorite_list'),
    path('favorite/add/', FavoriteAdd.as_view(), name='favorite_add'),
    path('favorite/<int:pk>/delete/', FavoriteDelete.as_view(), name='favorite_dalete'),
    
    path('book/<int:pk>/rating/list/', RatingList.as_view(), name='rating_list'),
    path('rating/create/', RatingCreate.as_view(), name='rating_create'),
    path('rating/<int:pk>/delete/', RatingDelete.as_view(), name='rating_delete'),

    path('cart/list/', CartList.as_view(), name='cart_list'),
    path('cart/add/', CartAdd.as_view(), name='cart_add'),
]