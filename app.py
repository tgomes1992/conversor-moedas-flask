from flask import Flask, render_template ,redirect , url_for ,request
from api_check import conversao


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route("/get_api",methods=['POST'])
def get_result():
    consulta = conversao(request.form['destino'], request.form['conversao'], request.form['tipoPagamento'])
    return render_template('resultado.html',resposta=consulta)




if __name__=='__main__':
    app.run(debug=True)