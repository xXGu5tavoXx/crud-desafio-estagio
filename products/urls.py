from django.urls import path
from . import views

urlpatterns = [
    # Rotas para Listar (GET) e Criar (POST)
    path('produtos/', views.produto_list_create, name='produto_list_create'),
    
    # Rotas para Detalhes (GET), Atualizar (PUT/PATCH) e Excluir (DELETE)
    path('produtos/<int:pk>/', views.produto_detail_update_delete, name='produto_detail_update_delete'),
    
    # Rota para Pesquisa (GET)
    path('produtos/search/', views.produto_search, name='produto_search'),
]
