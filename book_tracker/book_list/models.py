from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Author(models.Model): 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def full_name(self): 
        return f"{self.first_name} {self.last_name}"

    # setting display of Author to have first and last name in admin
    def __str__(self): 
        return self.full_name()


class Publisher(models.Model): 
    name = models.CharField(max_length=100)

class Book(models.Model): 
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    year_published = models.IntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, related_name="books")
    page_count = models.IntegerField()
    my_rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book-detail-page", args=[self.slug])

    def __str__(self): 
        return f"{self.title} ({self.my_rating})"
