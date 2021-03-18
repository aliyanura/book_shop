from rest_framework import serializers
from .models import *


class CategoriesSerializer(serializers.ModelSerializer):
    """Categories List"""

    class Meta:
        model = Category
        fields = ('id', 'title', )


class SubcategoriesSerializer(serializers.ModelSerializer):
    """Subcategories List"""

    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Subcategory
        fields = ('id', 'title', 'category')


class BookListSerializer(serializers.ModelSerializer):
    """Books list"""

    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    subcategory = serializers.SlugRelatedField(slug_field='title', read_only=True)
    middle_star = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price', 'category', 'subcategory', 'description', 'price', 'middle_star')
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all(), many=True).data
        return representation


class BookCreateSerializer(serializers.ModelSerializer):
    '''Book create'''

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price', 'category', 'subcategory', 'pub_house', 'pub_date', 'description')


class BookDetailSerializer(serializers.ModelSerializer):
    '''Book description'''

    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    subcategory = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price', 'category', 'subcategory', 'pub_house', 'pub_date', 'description')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all(), many=True).data
        representation['reviews'] = ReviewSerializer(instance.reviews.all(), many=True).data
        representation['rating'] = RatingDetailSerializer(instance.rating.all(), many=True).data
        return representation



class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AdImage
        fields = ('image', 'description')


class ReviewSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'message', 'created_at', 'created_by')


class RatingDetailSerializer(serializers.ModelSerializer):
    star = serializers.SlugRelatedField(slug_field='value', read_only=True)

    class Meta:
        model = Rating
        fields = ('id', 'star', 'book')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'star', 'book')



class ReviewCreateSerializer(serializers.ModelSerializer):
    '''Review create'''

    class Meta:
        model = Review
        fields = ('id', 'message', 'book')


class ReviewEditSerializer(serializers.ModelSerializer):
    '''Review edit'''

    class Meta:
        model = Review
        fields = ('message', )



class FavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'book')


class FavoriteSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Favorite
        fields = ('id', 'book')
    


class CartSerialiser(serializers.ModelSerializer):
    total_price = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'customer', 'total_price')
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['items'] = CartItemSerialiser(instance.items.all(), many=True).data
        return representation


class CartItemSerialiser(serializers.ModelSerializer):

    book = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = CartItem
        fields = ('id', 'book', 'quantity')