# importing flask
from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
import os
from werkzeug.utils import secure_filename

#####################from doc########################
ALLOWED_EXT = set(["csv"])

def allowed_file(filename):
    """check if uploaded file has the right extension"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXT


#############################################

app = Flask(__name__, static_url_path='/static')


# route to html page - "table"
@app.route("/")
def index():
    return render_template("index.html")


###################################################################


@app.route("/", methods=["POST"])
def upload():
    if request.method == "POST":
        f = request.files["file"]
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join("uploaded_File", filename))

            return redirect(url_for("table", filename=filename))

    return render_template("index.html")


@app.route("/table/<filename>")
def table(filename):
    upload_folder = os.path.join(os.getcwd(), "uploaded_File")
    file_path = os.path.join(upload_folder, filename)
    data = pd.read_csv(file_path, sep='[;,\t|:@]', engine='python')
    return render_template("table.html", tables=[data.to_html()], titles=[""])


if __name__ == "__main__":
    app.run(debug=True)
