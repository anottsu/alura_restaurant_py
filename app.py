from Modelos.restaurante import Restaurante
from Modelos.cardapio.bebida import Bebida
from Modelos.cardapio.prato import Prato


restaurante_01 = Restaurante('Sparrow','Marine')
# restaurante_02 = Restaurante('Tanjiro','Japanese')
# restaurante_03 = Restaurante('Bulls','Vegan')

# restaurante_01.alternar_estado()
# restaurante_01.receber_avaliacao('jay','10')
# restaurante_01.receber_avaliacao('law','10')


bebida_suco = Bebida("Suco melão", 5.00, "Grande")
prato = Prato("Misto", 3.00,"Quente")
restaurante_01.adicionar_no_cardapio(bebida_suco)
restaurante_01.adicionar_no_cardapio(prato)

def main():
    # Restaurante.listar_restaurantes()
    restaurante_01.exibir_cardapio
if __name__ == '__main__':
    main()

# teste com git

# modelos) (base) anottsu@anottsu:~/Documents/ALURA PYTHON/OO_Sabor_express$ git push -u origin master
# git@github.com: Permission denied (publickey).
# fatal: Could not read from remote repository.

# Please make sure you have the correct access rights
# and the repository exists.