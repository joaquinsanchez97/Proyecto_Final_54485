from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

#def home(request):
#    return render(request, 'home.html', {})

def LikeView(request, pk):
    post = Post.objects.get(id=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detalles-post', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all().order_by("name")
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def SobreNosotros(request):
    return render(request, 'sobre_nosotros.html')

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'lista_categorias.html', {'cat_menu_list':cat_menu_list})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category = cats.replace('-', ' '))
    context = {}
    context ['cats'] = cats.title().replace("-", "")
    context['category_posts'] = category_posts
    cat_menu = Category.objects.all()
    context['cat_menu'] = cat_menu
    return render(request, 'categorias.html', context)

class ArticuloDetailView(DetailView):
    model = Post
    template_name = "detalles_articulo.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all().order_by("name")
        context = super(ArticuloDetailView, self).get_context_data(*args, **kwargs)
        
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context['liked'] = liked
        return context

class AgregarPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'agregar_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all().order_by("name")
        context = super(AgregarPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AgregarCategoriaView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'agregar_categoria.html'
    fields = '__all__'
    #fields = ('title', 'body')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all().order_by("name")
        context = super(AgregarCategoriaView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class EditarPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'editar_post.html'
    #fields = ['title', 'title_tag', 'body']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all().order_by("name")
        context = super(EditarPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class EliminarPostView(DeleteView):
    model = Post
    template_name = 'eliminar_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all().order_by("name")
        context = super(DeleteView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'agregar_comentario.html'
    success_url = reverse_lazy('home')
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    