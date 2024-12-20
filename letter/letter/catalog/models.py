from django.db import models

from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000, help_text="내용을 입력하세요")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a> ')


    def __str__(self) :
        return self.title
    
    def get_absolute_url(self) :
        return reverse('book-detail', args=[str(self.id)])