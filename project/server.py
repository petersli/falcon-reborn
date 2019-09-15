from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return page_primer()

@app.route("/api/v1/runtime")
def runtime():
    return "xd"

def page_primer():
    with open("config.json") as json_file:
        data = json.load(json_file)

    input_type, output_type = data["input"].split(".")[0], data["output"].split(".")[0]
    input_size = [int(value) for value in data["input"].split(".")[1].split("x")]
    output_size = [int(value) for value in data["output"].split(".")[1].split("x")]

    return render_template("index.html", input=str(input_size), output=str(output_size))


