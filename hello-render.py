from flask import render_template, Flask, request, redirect, url_for
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

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

# def get_plot():
#     recent_data = yf.download("AAPL", period="30d")
#     plt.plot(np.arange(1,31),recent_data)
#     return plt

@app.route('/apple-stock')
def show_stock():
    # plot = get_plot()
    # plot.savefig(os.path.join('static', 'images', 'plot.png')) 
    recent_data = yf.download("AAPL", period="30d")
    plt.plot(np.arange(1,31),recent_data)

    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    plt.close()

    img_base64 = base64.b64encode(img_bytes.read()).decode('utf-8')

    return render_template('apple-stock.html', img_data=img_base64)

if __name__ == "__main__":
   app.run(debug=True)