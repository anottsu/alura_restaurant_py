from abc import ABC, abstractmethod     #import abstract method

class ItemCardapio(ABC):                # if get methods from ABC is necessary have the inherit (ABC)
    def __init__(self,nome,preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self): # Here isn't necessary to be implement code, because  is just a model. although is madantory implement the abstract method into all items from cardapio or the code is crash.
        pass








        # O CODIGO DEVERIA NÃO FUNCIONAR.... VERIFICAR O PQ JA QUE CRIEI UM ABSTRACT E ISSO DEVERIA SER MANDATORIO PARA TODOS OS PRODUTOS.