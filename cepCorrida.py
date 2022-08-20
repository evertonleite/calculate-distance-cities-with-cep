from pycep_correios import get_address_from_cep, WebService, exceptions
import googlemaps
import re

api_key = 'AIzaSyA2q035Meede4sQ6jde84BGysxvXpDalmI'

#recebe o cep
cepOrigem = input("Digite o CEP da origem: ")
cepDestino = input("Digite o CEP do destino: ")

def trataCep(cep):
    #limita a variável com a quantidade de caracteres específica
    saida = cep[0:9]
    #retira caracteres especiais e letras, deixando apenas números
    cepTratado = re.sub(r"[^0-9]","", saida)
    
    return cepTratado

def verificaCep(cepRecebido):
    try:
        cep = get_address_from_cep(cepRecebido, webservice=WebService.CORREIOS)
        cidadeCep = cep['cidade']
        print(cidadeCep)
        
    except exceptions.InvalidCEP as eic:
        print(eic)
        return eic

    except exceptions.CEPNotFound as ecnf:
        print(ecnf)
        return ecnf

    except exceptions.ConnectionError as errc:
        print(errc)
        return errc

    except exceptions.Timeout as errt:
        print(errt)
        return errt

    except exceptions.HTTPError as errh:
        print(errh)
        return errh

    except exceptions.BaseException as e:
        print(e)
        return e
        
    return cidadeCep

def calculaCorrida(origem, destino):   
    gmaps = googlemaps.Client(key=api_key) 
    my_dist = gmaps.distance_matrix(origem,destino)['rows'][0]['elements'][0] 
    print(my_dist)
    
    distancia = my_dist['distance']
    valorDistancia = distancia['value']
    
    valorKm = 2.50 * (valorDistancia / 1000)
    
    print('Custa R$', valorKm)
    

cep1 = trataCep(cepOrigem)
cep2 = trataCep(cepDestino)

print(cep1)
print(cep2)
    

if (verificaCep(cep1) == ''):
    print('CEP Origem inválido')
elif(verificaCep(cep2) == ''):
    print('CEP Destino inválido')
else:
    origem = verificaCep(cep1)
    destino = verificaCep(cep2)
    calculaCorrida(origem, destino)