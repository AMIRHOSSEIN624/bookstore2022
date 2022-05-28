from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Book(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    text = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=3)
    cover = models.ImageField(upload_to='covers/')
    favorite = models.ManyToManyField(get_user_model(), related_name='favorite', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_page', args=[self.id])


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
