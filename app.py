from flask import Flask, render_template
import csv
 
app = Flask(__name__)

@app.route("/")
def index():
  with open("insurance1.csv") as file:
    reader = csv.reader(file)
    return render_template("index.html", csv=reader)
 
if __name__ == '__main__':
    app.run(debug=True)