from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de ejemplo
elementos = ["Aprender Python", "Hacer el reto", "Tomar café"]

@app.route('/')
def index():
    return render_template('index.html', elementos=elementos)

@app.route('/agregar', methods=['POST'])
def agregar():
    nuevo_elemento = request.form.get('elemento')
    if nuevo_elemento:
        elementos.append(nuevo_elemento.strip())
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)