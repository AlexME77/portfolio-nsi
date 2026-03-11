from flask import Flask, request, render_template, send_file
from PIL import Image, ImageDraw
from io import BytesIO

app = Flask(__name__)


@app.route('/')
def index():
    """
    Traite les requêtes HTTP de la ressource dont l'url est "/"
    Revoie le contenu de la réponse HTTP
    """
    return render_template("index.html")


@app.route('/exemple_traitement_1', methods=['POST', 'GET'])
def traitement_1():
    """
    Traite les requêtes HTTP de la ressource dont l'url est "/exemple_traitement_1"
    Revoie le contenu de la réponse HTTP
    """

    # Récupération du paramètre transmis en POST
    if request.form.get('nom'):
        return "Paramètre \"nom\" bien reçu : " + request.form.get('nom')
    # Récupération du paramètre transmis en GET
    elif request.args.get('nom'):
        return "Le paramètre \"nom\" (" + request.args.get('nom') + ") doit être envoyé selon la méthode POST."
    # Réponse par défaut
    else:
        return "En attente du paramètre \"nom\"."


@app.route('/exemple_traitement_2', methods=['POST', 'GET'])
def traitement_2():
    """
    Traite les requêtes HTTP de la ressource dont l'url est "/exemple_traitement_2"
    Revoie le contenu de la réponse HTTP
    """

    # Récupération du paramètre transmis en POST
    if request.form.get('nom'):
        texte = "Paramètre \"nom\" bien reçu : " + request.form.get('nom')
    # Récupération du paramètre transmis en GET
    elif request.args.get('nom'):
        texte = "Le paramètre \"nom\" (" + request.args.get('nom') + ") doit être envoyé selon la méthode POST."
    # Réponse par défaut
    else:
        texte = "En attente du paramètre \"nom\"."

    return render_template("reponse.html", message=texte)


@app.route('/exemple_traitement_3', methods=['POST', 'GET'])
def traitement_3():
    """
    Traite les requêtes HTTP de la ressource dont l'url est "/exemple_traitement_3"
    Revoie le contenu de la réponse HTTP
    """
    if request.values.get('nom'):
        nom = request.values.get('nom')
    else:
        nom = "Hello, World!"

    largeur = 400
    hauteur = 400
    image = Image.new('RGB', (largeur, hauteur), color='white')

    dessin = ImageDraw.Draw(image)
    dessin.text((20, hauteur / 2), nom, fill=(0, 0, 0))
    dessin.line([(10, hauteur / 2), (largeur - 20, hauteur / 2)], fill="black", width=0)
    dessin.line([(10, hauteur / 2 + 10), (largeur - 20, hauteur / 2 + 10)], fill="black", width=0)

    # Envoi de l'image
    fichier_memoire = BytesIO()
    image.save(fichier_memoire, 'PNG')
    fichier_memoire.seek(0)
    return send_file(fichier_memoire, mimetype='image/png')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
