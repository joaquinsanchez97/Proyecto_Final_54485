
from django.urls import path, include
#from . import views
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('articulo/<int:pk>', ArticuloDetailView.as_view(), name="detalles-post"),
    path('agregar_post/', AgregarPostView.as_view(), name="agregar-post"),
    #path('agregar_categoria/', AgregarCategoriaView.as_view(), name="agregar-categoria"),
    path('articulo/editar/<int:pk>', EditarPostView.as_view(), name="editar-post"),
    path('articulo/<int:pk>/eliminar', EliminarPostView.as_view(), name="eliminar-post"),
    path('categorias/<str:cats>/', CategoryView, name="categoria"),
    path('lista-categorias/', CategoryListView , name="lista-categorias"),
    path('like/<int:pk>', LikeView, name='like_post'),
    #path('<int:pk>/password/', auth_views.PasswordChangeView.as_view(template_name="cambiar-contraseña.html")),
    path('', include('members.urls')),
    path('articulo/<int:pk>/comentar/', AddCommentView.as_view(), name="agregar-comentario"),
    path('sobre-nosotros', SobreNosotros, name='sobre-nosotros'),

]
