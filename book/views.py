from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import *
from .serializers import *
from .models import *
from .filter import *
from .pagination import PaginationBooks
from django.db import models
from django.contrib.auth import get_user_model


class CategoriesList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    

class CategoryBooks(generics.ListAPIView):
    serializer_class = BookListSerializer

    def get_queryset(self, *args, **kwargs):
        books = Book.objects.filter(category__pk=self.kwargs['pk'])
        return books


class SubategoriesList(generics.ListAPIView):
    serializer_class = SubcategoriesSerializer

    def get_queryset(self, *args, **kwargs):
        subcategories = Subcategory.objects.filter(category__pk=self.kwargs['pk'])
        return subcategories


class SubategoryBooks(generics.ListAPIView):
    serializer_class = BookListSerializer

    def get_queryset(self, *args, **kwargs):
        books = Book.objects.filter(subcategory__pk=self.kwargs['pk']).annotate(
            middle_star = models.Sum(models.F('rating__star'))/models.Count(models.F('rating'))
        )
        return books



class BooksList(generics.ListAPIView):
    """Books list output"""
    serializer_class = BookListSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend, )
    filterset_class = BookFilter
    pagination_class = PaginationBooks
    search_fields = ['title', 'author']

    def get_queryset(self):
        books = Book.objects.all().annotate(
            middle_star = models.Sum(models.F('rating__star'))/models.Count(models.F('rating'))
        )
        return books


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    http_method_names = ['get',]


class BookCreate(generics.CreateAPIView):
    serializer_class = BookCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    http_method_names = ['post',]



class BookEdit(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    http_method_names = ['patch',]


class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    http_method_names = ['delete',]



class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer
    # permission_classes = [IsAuthenticated, ]
    http_method_names = ['post',]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ReviewDetail(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ['get',]


class ReviewEdit(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewEditSerializer
    permission_classes = [IsReviewOwner, ]
    http_method_names = ['patch',]


class ReviewDelete(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsReviewOwner, ]
    http_method_names = ['delete',]



class FavoriteList(generics.ListAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        favorites = Favorite.objects.filter(owner=self.request.user)
        return favorites


class FavoriteAdd(generics.CreateAPIView):
    serializer_class = FavoriteCreateSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['post',]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavoriteDelete(generics.DestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteCreateSerializer
    permission_classes = [IsOwner, ]
    http_method_names = ['delete',]



class RatingList(generics.ListAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self, *args, **kwargs):
        ratings = Rating.objects.filter(book__pk=self.kwargs['pk'])
        return ratings
    

class RatingCreate(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['post',]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RatingDelete(generics.DestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsOwner, ]
    http_method_names = ['delete',]


class CartList(generics.ListAPIView):
    serializer_class = CartSerialiser

    def get_queryset(self):
        cart = Cart.objects.filter(customer__id = self.request.user.id).annotate(
            total_price = models.Sum(models.F('items__book__price')*models.F('items__quantity'))
        )
        return cart
        

class CartAdd(generics.CreateAPIView):
    serializer_class = CartSerialiser
    # permission_classes = [IsAuthenticated, ]
    http_method_names = ['post',]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)