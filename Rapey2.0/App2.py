from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def index_Repartidor():
    return render_template('sesion-repartidor.html')

if __name__ == '__main__':
    app.run(port=3001,debug=True)