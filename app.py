from Modelos.restaurante import Restaurante
from Modelos.cardapio.bebida import Bebida
from Modelos.cardapio.prato import Prato
from Modelos.cardapio.sobremesa import Sobremesa


restaurante_01 = Restaurante('Sparrow','Marine')
bebida_suco = Bebida("Suco melão", 5.00, "Grande")
bebida_suco.aplicar_desconto()
prato = Prato("Misto", 2.00,"Quente")
prato.aplicar_desconto()
sobremesa = Sobremesa('Pudim',3.00,"caramelo")
sobremesa.aplicar_desconto()
restaurante_01.adicionar_no_cardapio(bebida_suco)
restaurante_01.adicionar_no_cardapio(prato)
restaurante_01.adicionar_no_cardapio(sobremesa)

def main():
    # Restaurante.listar_restaurantes()
    restaurante_01.exibir_cardapio
if __name__ == '__main__':
    main()

#criado o item sobremesa