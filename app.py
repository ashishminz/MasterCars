from flask import Flask, render_template, request
import pandas as pd
import mysql.connector

# Initialize Flask app
app = Flask(__name__)


# Database connection configuration
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='testdb'
    )
    return connection


@app.route('/')
def index():
    # Fetch data from MySQL and convert it to Pandas DataFrame
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)

    # Render the index.html template with the data from MYSQL
    return render_template('index.html', data=df.to_html())


if __name__ == '__main__':
    app.run(debug=True)