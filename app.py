from flask import Flask, render_template

app = Flask(__name__)  # __name__ est une variable gérée par python


@app.route('/')  # représente la racine du site
def index():  # le nom n’est pas important pour le système
    return render_template("index.html")


@app.route('/creation.html')  # représente la racine du site
def creation():  # le nom n’est pas important pour le système
    return render_template("creation.html")


@app.route('/pardefaut.html')  # représente la racine du site
def pardefaut():  # le nom n’est pas important pour le système
    return render_template("pardefaut.html")


@app.route('/personnages.html')  # représente la racine du site
def personnages():  # le nom n’est pas important pour le système
    return render_template("personnages.html")


if __name__ == "__main__":  # lance l’application
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
