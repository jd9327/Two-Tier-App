import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL from environment variables
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'default_user')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'default_password')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'default_db')

# Initialize MySQL
mysql = MySQL(app)

def init_db():
    with app.app_context():
        cur = mysql.connection.cursor()
        # Creating user_info table if it doesn't exist
        cur.execute('''
        CREATE TABLE IF NOT EXISTS user_info (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            city VARCHAR(100) NOT NULL,
            state VARCHAR(100) NOT NULL,
            country VARCHAR(50) DEFAULT 'India' NOT NULL
        );
        ''')
        mysql.connection.commit()
        cur.close()

@app.route('/')
def hello():
    cur = mysql.connection.cursor()
    # Fetch all records from user_info
    cur.execute('SELECT name, city, state, country FROM user_info')
    user_info = cur.fetchall()
    cur.close()
    return render_template('index.html', user_info=user_info)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    city = request.form.get('city')
    state = request.form.get('state')
    
    cur = mysql.connection.cursor()
    # Insert new user info into the user_info table
    cur.execute('INSERT INTO user_info (name, city, state) VALUES (%s, %s, %s)', (name, city, state))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'name': name, 'city': city, 'state': state})

if __name__ == '__main__':
    init_db()  # Initialize the user_info table
    app.run(host='0.0.0.0', port=5000, debug=True)

