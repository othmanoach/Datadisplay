from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploaded_csvFiles"

if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])


def allowed_file(file_name):
    """vérifier l'extension du fichier"""
    return "." in file_name and file_name.rsplit(".", 1)[1].lower() == "csv"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def upload_file():
    print("test")
    if request.method == "POST":
        filename = request.files["filename"]
        if allowed_file(filename):
            df = pd.read_csv(filename)
            print(df.head())
            return render_template("index.html")

    else:
        return render_template("index.html")


# route pour afficher la table des données du fichier importé
@app.route("/table/<string:file_name>")
def table(file_name):
    return render_template("table.html", file_name=file_name)


if __name__ == "__main__":
    app.run(debug=True)
