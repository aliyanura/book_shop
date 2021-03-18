from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=150)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'categories'
    

class Subcategory(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'subcategories'


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    price = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='books')
    pub_house = models.CharField(max_length=150)
    pub_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-pub_date',)


class Review(models.Model):
    message = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book}'


class Star(models.Model):
    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.value}'


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='rating')
    star = models.ForeignKey(Star, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owner}'

class Favorite(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='favorites')


class AdImage(models.Model):
    image = models.ImageField(upload_to='books')
    book = models.ForeignKey(Book, related_name='images', on_delete=models.CASCADE)
    description = models.CharField(max_length=55)

    def __str__(self):
        if self.image:
            return self.image.url
        return ''


class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
            return f'{self.customer}'

class CartItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
