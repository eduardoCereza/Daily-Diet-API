from flask import Flask
from models.snack import Snack

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #Caminho do banco de dados

if __name__ == '__main__':
    app.run(debug=True)