from Modelos.cardapio.item_cardapio import ItemCardapio  #É PARA NAVEGAR ATE O LOCAL QUE DESEJA UTILIZAR#

class Prato(ItemCardapio):   # THE CLASS PRATO INHERITS METHODS AND CLASS FROM Item.Cardapio#
    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco)
        self.descricao = descricao

   # View on screen like string
    def __str__(self):
        return self._nome


    #OBJECTIVE: SET THIS PROJECT TO GITHUB VIA GIT...#