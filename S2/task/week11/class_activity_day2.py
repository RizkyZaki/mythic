from flask import Flask
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    html = "Selamat Datang"
    html = html + "<br><a href='/graph'>Penjualan Avanza</a>"
    html = html + "<br><a href='/profit'>Keuntungan Penjualan</a>"
    return html

@app.route('/graph')
def plot():
    df = pd.read_csv("raw-data/penjualan_mobil_avanza.csv", sep=';')

    # Membuat plot
    plt.plot(df['Tahun'], df['Penjualan'], color="green", marker='o', linestyle='-')

    plt.xlabel('Tahun')
    plt.ylabel('Penjualan')
    plt.title('Grafik Penjualan Mobil Avanza')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    img_str = base64.b64encode(buffer.read()).decode('utf-8')

    plt.close()

    return f'<img src="data:image/png;base64,{img_str}">'
@app.route('/profit')
def profit():
    df = pd.read_csv("raw-data/data-penjualan-avanza.csv", sep=';')

    # Membuat plot
    plt.plot(df['Tahun'], df['Penjualan'], color="green", marker='o', linestyle='-')
    
    for i, txt in enumerate(df['Penjualan']):
        plt.annotate(txt, (df['Tahun'][i], df['Penjualan'][i]), textcoords="offset points", xytext=(0,10), ha='center')

    plt.xlabel('Tahun')
    plt.ylabel('Penjualan')
    plt.title('Grafik Penjualan Mobil Avanza')

    plt.xticks(rotation=45)
    plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    img_str = base64.b64encode(buffer.read()).decode('utf-8')

    plt.close()

    return f'<img src="data:image/png;base64,{img_str}">'
  
if __name__ == '__main__':
    app.run(debug=True)
