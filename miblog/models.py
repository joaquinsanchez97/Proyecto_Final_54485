from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        #return reverse('detalles-articulo', args=(str(self.id)))
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(verbose_name="Título", max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    snippet = models.CharField(max_length=255, verbose_name="Subtítulo")
    title_tag = models.CharField(verbose_name="Tag", max_length=255)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Autor",)
    body = RichTextField(blank=True, null=True, verbose_name="Cuerpo")
    #body = models.TextField(verbose_name="Cuerpo")
    post_date = models.DateField(auto_now_add=True, verbose_name="Fecha")
    category = models.CharField(max_length=255, default='sin categoría', verbose_name="Categoría")
    likes = models.ManyToManyField(User, related_name = 'blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        #return reverse('detalles-articulo', args=(str(self.id)))
        return reverse('home')
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    