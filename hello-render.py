from flask import render_template, Flask, request
import yfinance as yf

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    recent_data = yf.download("AAPL", period="1d")
    return render_template('hello-world.html', name=name)

# @app.route('/stock/')
# def stock():
#     symbol = request.args.get('symbol', default="AAPL")
#     quote = yf.Ticker(symbol)
#     return quote.info 

@app.route('/hello', methods=['POST']) 
def stock():
    recent_data = yf.download("AAPL", period="1d")
    return recent_data

@app.route("/") 
def index(): 
    return "Main Page"

if __name__ == "__main__":
   app.run(debug=True)