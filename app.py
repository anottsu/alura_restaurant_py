# from Modelos.restaurante import Restaurante
# from Modelos.cardapio.bebida import Bebida
# from Modelos.cardapio.prato import Prato
# from Modelos.cardapio.sobremesa import Sobremesa

import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response =requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {} # Dictionary

    for item in dados_json: # percorre o arquivo json
        nome_do_restaurante = item ['Company']   # cria uma lista para armazenar o 'Company' do Json
        if nome_do_restaurante not in dados_restaurante:  # verifica se ja existe o 'Company' no dicionario dados restaurante
            dados_restaurante[nome_do_restaurante] =[]  # se nao existir cria uma lista nova com o 'Company'

        dados_restaurante[nome_do_restaurante].append({ # adiciona item,price e descrição ao dicionario atraves da chave 'Company'
            "item":item['Item'],
            "price":item['price'],
            "description":item['description']
        })

else :
    'page not found' 

print(dados_restaurante['McDonald’s']) 

# restaurante_01 = Restaurante('Sparrow','Marine')
# bebida_suco = Bebida("Suco melão", 5.00, "Grande")
# bebida_suco.aplicar_desconto()
# prato = Prato("Misto", 2.00,"Quente")
# prato.aplicar_desconto()
# sobremesa = Sobremesa('Pudim',3.00,"caramelo")
# sobremesa.aplicar_desconto()
# restaurante_01.adicionar_no_cardapio(bebida_suco)
# restaurante_01.adicionar_no_cardapio(prato)
# restaurante_01.adicionar_no_cardapio(sobremesa)

def main():
    # Restaurante.listar_restaurantes()
    # restaurante_01.exibir_cardapio
    pass
if __name__ == '__main__':
    main()

#criado o item sobremesa