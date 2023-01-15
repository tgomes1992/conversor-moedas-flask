import requests
import json


class ConversorApi:
    def calculo_taxa(self,tipo,valor):
        if tipo=="Boleto":
            return float(valor) * 0.0145
        elif tipo=="Cartao":
            return float(valor) * 0.0763


    def taxaconversao(self,valor):
        if float(valor) <= 3000 :
            return float(valor) * 0.02
        elif float(valor)>3000 :
            return float(valor) * 0.01

    def empty_dict(self):
        resultado = {
            'origem': 'BRL',
            'destino': "" ,
            'valor': f"R$ ",
            'taxa_compra': "",
            'pagamento': "",
            'valor_conversão': "",
            'taxapagto': "",
            'taxaconversao': "",
            'conversao-taxas': ""
        }
        return resultado

    def conversao(self, destino,valor,pagamento):
        busca = f"https://economia.awesomeapi.com.br/last/{destino}-BRL"
        request_resultado = requests.get(busca).content.decode("utf-8")
        bid = json.loads(request_resultado)[f'{destino}BRL']['bid']
        base_conversao = round(float(valor) - self.taxaconversao(valor) - self.calculo_taxa(pagamento, valor),2)

        resultado = {
            'origem': 'BRL',
            'destino': destino ,
            'valor': f"R$ {valor}",
            'taxa_compra': bid,
            'pagamento': "Cartão de Crédito" if pagamento=="Cartao" else pagamento ,
            'valor_conversão': round(base_conversao/float(bid),2),
            'taxapagto': round(self.calculo_taxa(pagamento, valor),2) ,
            'taxaconversao': round(self.taxaconversao(valor)),
            'conversao-taxas': base_conversao
        }

        return resultado







