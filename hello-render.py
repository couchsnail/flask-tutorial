from flask import render_template, Flask, request, redirect, url_for
import yfinance as yf

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    #recent_data = yf.download("AAPL", period="1d")
    return render_template('hello-world.html', name=name)

@app.route('/open_new_tab', methods=['POST'])
def open_new_tab():
    return redirect("https://google.com")

@app.route('/hello/print_info',methods=['POST'])
def print_info():
    stocks = str(yf.Ticker("AAPL").info['currentPrice'])
    return stocks

@app.route("/") 
def index(): 
    return "Main Page"

if __name__ == "__main__":
   app.run(debug=True)