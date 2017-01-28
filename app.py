import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)

def get_csv():
    csv_path ="./static/top50weu.csv"
    #adding encoding because of issues with it. http://stackoverflow.com/questions/12468179/unicodedecodeerror-utf8-codec-cant-decode-byte-0x9c
    csv_file = open(csv_path, "r", encoding="latin-1")
    #parsed and returned as a list of dictionaries
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

@app.route("/")
def index():
    template ="index.html"
    object_list = get_csv()
    return render_template(template, object_list=object_list)

@app.route("/<row_id>/")
def detail(row_id):
    template = "detail.html"
    object_list = get_csv()
    for row in object_list:
        if row["id"] == row_id:
            return render_template(template, object=row)

if __name__ == "__main__":
    #Fire up the Flask test server
    app.run(debug=True, use_reloader=True)
