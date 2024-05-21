from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    # Koneksi ke database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="week11"
    )
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM customer")
    myresult = mycursor.fetchall()

    # Render template dan kirim data
    return render_template('customers.html', customers=myresult)

if __name__ == '__main__':
  app.run(debug=True)