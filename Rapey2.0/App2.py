from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'rapey'
mysql = MySQL(app)

#Configuraciones
app.secret_key = 'mysecretkey'

#CRUD Repartidores
@app.route('/')
def index_Repartidor():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM repartidor')
    datos = cursor.fetchall
    return render_template('sesion-repartidor.html', repartidor = datos)

@app.route('/agregar_repartidor', methods = ['POST'])
def agregar_repartidor():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        rut = request.form['Rut']
        region = request.form['Region']
        telefono = request.form['Telefono']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO repartidor (Nombre_repartidor, Rut_repartidor, Nro_region, telefono) VALUES (%s, %s, %s, %s)',
        (nombre,rut,region,telefono))
        mysql.connection.commit()
        flash('Repartidor agregado correctamente')
        return redirect(url_for('index_Repartidor'))

if __name__ == '__main__':
    app.run(port=3001,debug=True)