from flask import Flask
from models.snack import Snack

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)