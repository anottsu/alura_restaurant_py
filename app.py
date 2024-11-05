# from Modelos.restaurante import Restaurante
# from Modelos.cardapio.bebida import Bebida
# from Modelos.cardapio.prato import Prato
# from Modelos.cardapio.sobremesa import Sobremesa

import requests
import json

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

for nome_do_restaurante, dados in  dados_restaurante.items():  # variaveis criadas nome_do_restaurante e dados, elas vao iterar sobre dados_restaurante.items()
    nome_do_arquivo =f'{nome_do_restaurante}.json'              # nome_do_Arquivo + formatação em string + a extensão .json
    with open(nome_do_arquivo,'w') as file_restaurant: # abre e depois de executar, fecha o arquivo  para evitar corromper, nome do arquivo  + write , nome temporario do arquivo
        json.dump(dados,file_restaurant,indent=4) # grava no formato json os dados passados. edentação



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