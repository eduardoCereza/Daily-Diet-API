from flask import Flask, request, jsonify
from models.snack import Snack
from database import db
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #Caminho do banco de dados

db.init_app(app)
#CREATE
@app.route("/snack", methods=['POST'])
def create_snack():
    data = request.json
    
    name = data.get('name')
    description = data.get('description')
    hasDiet = data.get('hasDiet')
    
    if name and description and hasDiet:
        snack = Snack(name=name, description=description, date=datetime.now(), hasDiet=hasDiet)
        db.session.add(snack)
        db.session.commit()
        return jsonify({"message": "Refeição criada com sucesso!"})
    
    return jsonify({"message": "Campos vazios!"}), 400

#UPDATE
@app.route("/snack/<int:id>", methods=['PUT'])
def update_snack(id):
    data = request.json
    
    snack = Snack.query.get(id)
    
    if snack :
        snack.name = data['name']
        snack.description = data['description']
        snack.hasDiet = data['hasDiet']
        
        db.session.commit()
        return jsonify({"message": f"Refeição atualizada com sucesso!"})
    
    return jsonify({"message": "Refeição não encontrado"}), 404
    
@app.route("/snack/<int:id>", methods=['DELETE'])
def delete_snack(id):
    snack = Snack.query.get(id)
    
    if snack:
        db.session.delete(snack)
        db.session.commit()
        
        return jsonify({"message": f"Refeição deletada com sucesso!"})
    return jsonify({"message": "Refeição não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)