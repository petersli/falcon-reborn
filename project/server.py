from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import json, os, random, string
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return page_primer()

@app.route("/api/v1/runtime", methods=["POST"])
def runtime():
    file = request.files["file"]
    extension = os.path.splitext(file.filename)[1]
    filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    secure_filename("static/input/"+filename+extension)
    file.save("static/input/"+filename+extension)
    return "Success", 200

def page_primer():
    with open("config.json") as json_file:
        data = json.load(json_file)

    input_type, output_type = data["input"].split(".")[0], data["output"].split(".")[0]
    input_size = [int(value) for value in data["input"].split(".")[1].split("x")]
    output_size = [int(value) for value in data["output"].split(".")[1].split("x")]

    return render_template("index.html", input=str(input_size), output=str(output_size), page_info=data["page_info"], page_subheading=data["page_subheading"])


