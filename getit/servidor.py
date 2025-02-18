from flask import Flask, render_template, request, redirect,  render_template_string,flash
import sqlite3 as sql


app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from texto")
    data=cur.fetchall()
    return render_template('index.html', datas=data)

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form['titulo']  # Obtém o valor do campo 'titulo'
    detalhes = request.form['detalhes']  # Obtém o valor do campo 'detalhes'
    con = sql.connect("db_web.db")
    cur = con.cursor()
    cur.execute("INSERT INTO texto (titulo, detalhes) VALUES (?, ?)", (titulo, detalhes))
    con.commit()
    return redirect('/')
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    con = sql.connect("db_web.db")
    cur = con.cursor()
    cur.execute("DELETE FROM texto WHERE id = ?", (id,))
    con.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)