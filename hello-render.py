from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/hello-render/')
@app.route('/hello-render/<name>')
def hello(name=None):
    return render_template('hello-world.html', name=name)

@app.route("/") 
def index(): 
    return "Main Page"

if __name__ == "__main__":
   app.run()