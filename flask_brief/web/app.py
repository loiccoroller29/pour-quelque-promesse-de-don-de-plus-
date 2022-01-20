
from flask import Flask, render_template, request
import data


app = Flask(__name__)

@app.route('/')
def page_principal():
    return render_template('page_principale.html')

@app.route('/page_don')
def page_don():
   return render_template('page_dons.html')

@app.route('/page_datas', methods = ['GET'])
def page_datas():
    don = data.lire_pages_dont()
    result=request.form
    return render_template('page_data.html', dont=don)

@app.route('/<int:don_id>')
def don(don_id):
    don = data.set_dons(don_id)
    return render_template('page_data.html', dons=don)    


@app.route('/page_data', methods=['GET'])
def page_data():
    nom = request.values.get('nom')
    prenom = request.values.get('prenom')
    adresse = request.values.get('adresse')
    mail = request.values.get('mail')
    somme = request.values.get('somme')
    don = data.lire_pages_dont()
    data.set_datas(nom, prenom, adresse, mail, somme)
    total=data.somme()
    return render_template('page_data.html', dons=don, total=total)


    
if __name__ =="__main__":
    app.run(debug=True)