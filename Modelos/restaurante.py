import os
import csv
from Modelos.avaliacao import Avaliacao
from Modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:

    restaurantes = []
    
    def __init__(self, nome,categoria):
        
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self) # faz o append  do proprio restaurante    
    
    def __str__(self):
        return f"{self._nome} | {self._categoria}"
    
    @classmethod
    def listar_restaurantes(cls):

        print(f"{'Nome'.ljust(22)} | {'Categoria'.ljust(22)} | {'Avaliação'.ljust(25)} | Status")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(22)} | {restaurante._categoria.ljust(22)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}")

    @property
    def ativo(self):
        return'✅'if self._ativo else '❎'
    

    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self,cliente,nota):
         if 0 < int(nota) <= 5:

            avaliacao = Avaliacao(cliente,nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return "---"
        
        # soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        soma_das_notas = sum(float(avaliacao._nota) for avaliacao in self._avaliacao)
        qtd_notas =len(self._avaliacao)
        media = round(soma_das_notas / qtd_notas, 1)
        return media
    

    def adicionar_no_cardapio(self,item):
            if isinstance(item,ItemCardapio):
                self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        print(f"Menu do Restaurante {self._nome}\n")
        for i,item in enumerate(self._cardapio,start=1):
           
            if hasattr(item,'descricao'): 
                  mensagem_prato = f"{i}. Nome: {item._nome} | Preço R$: {round(item._preco,2)} | Descrição: {item.descricao}" 
                  print(mensagem_prato) 

            elif hasattr(item,'descricao'): 
                mensagem_sobremesa = f"{i}. Nome: {item._nome} | Preço R$: {round(item._preco,2)} | Descrição: {item.descricao}" 
                print(mensagem_sobremesa)

            else:
                mensagem_bebida = f"{i}. Nome: {item._nome} | Preço R$: {round(item._preco,2)} | Tamanho: {item.tamanho}" 
                print(mensagem_bebida)  


#elif add para sobremesa com mensagem