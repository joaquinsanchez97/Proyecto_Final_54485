from django import forms
from .models import Post, Category, User, Comment

#choices = [('Pagos', 'Pagos'), ('Cobros', 'Cobros'), ('Logística', 'Logística'), ('Plataformas', 'Plataformas'), ('Ventas', 'Ventas'), ('ExportaSimple', 'ExportaSimple'), ('Courier', 'Courier')]
choices = Category.objects.all().values_list('name','name')
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'snippet', 'title_tag', 'header_image', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),  
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'usuario', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'category': forms.Select(choices = choice_list, attrs={'class': 'form-control', 'placeholder': ''}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'En este espacio podrás escribir el contenido de tu blog post'}), 
 
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'snippet', 'title_tag', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),  
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'category': forms.Select(choices = choice_list, attrs={'class': 'form-control', 'placeholder': ''}),
            #'author': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'En este espacio podrás escribir el contenido de tu blog post'}),  
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ''}),  
        }