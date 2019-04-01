from django.urls import path
from .views import lista_pessoas
from .views import nova_pessoa
from .views import atualizar_pessoa
from .views import deletar_pessoa

urlpatterns = [
    path('lista-pessoas/', lista_pessoas, name='lista_pessoas'),
    path('nova-pessoa/', nova_pessoa, name='nova_pessoa'),
    path('atualizar-pessoa/<int:id>/', atualizar_pessoa, 
          name='atualizar_pessoa'),
    path('deletar-pessoa/<int:id>/', deletar_pessoa, 
          name='deletar_pessoa')
]
