import requests
import json


def calculo_taxa(tipo,valor):
    if tipo=="Boleto":
        return float(valor) * 0.0145
    elif tipo=="Cartao":
        return float(valor) * 0.0763


def taxaconversao(valor):
    if float(valor) <= 3000 :
        return float(valor) * 0.02
    elif float(valor)>3000 :
        return float(valor) * 0.01
    


def conversao(destino,valor,pagamento):
    busca = f"https://economia.awesomeapi.com.br/last/{destino}-BRL"
    request_resultado = requests.get(busca).content.decode("utf-8")
    bid = json.loads(request_resultado)[f'{destino}BRL']['bid']
    base_conversao = round(float(valor) - taxaconversao(valor) - calculo_taxa(pagamento, valor),2)

    resultado = {
        'origem': 'BRL',
        'destino': destino ,
        'valor': f"R$ {valor}" ,
        'taxa_compra': bid,
        'pagamento': "Cartão de Crédito" if pagamento=="Cartao" else pagamento ,
        'valor_conversão': round(base_conversao/float(bid),2), 
        'taxapagto': round(calculo_taxa(pagamento, valor),2) ,  
        'taxaconversao': round(taxaconversao(valor)),
        'conversao-taxas': base_conversao
    }

    return (resultado)







