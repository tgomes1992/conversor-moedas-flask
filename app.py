from flask import Flask, render_template ,redirect , url_for ,request
from api_check import ConversorApi


app = Flask(__name__)

@app.route('/',  methods=["GET",'POST'])
def main():
    api = ConversorApi()
    print (request.form)
    if request.method =="POST":
        consulta = api.conversao(request.form['destino'], request.form['conversao'], request.form['tipoPagamento'])
    else:
        consulta = api.empty_dict()
    return render_template('main.html' , resposta=consulta)


