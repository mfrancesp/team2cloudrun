from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect
from flask_migrate import Migrate
from sqlalchemy import create_engine
import mysql.connector
from mysql.connector import Error
from sqlalchemy.engine.base import Connection


app = Flask(__name__)

db_user = "user1"
db_password = "1234"
db_name = "testing"
db_connection_name = "team2-353417:europe-west1:databaseuser"
host = "35.205.41.62"
#unix_socket = '/cloudsql/{}'.format(db_connection_name)
#engine_url = 'mysql+pymysql://{}:{}@/{}?unix_socket={}'.format(db_user, db_password, db_name, unix_socket)

engine_url = 'mysql+pymysql://{}:{}@{}/{}'.format(db_user, db_password, host, db_name)

engine = create_engine(engine_url)



@app.route('/')
def start():
    query="SELECT * FROM dates"
    with engine.connect() as connection:
        entries=connection.execute(query).fetchall()
        
        return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form=request.form
        title=str(form.get('title'))
        description=str(form.get('description'))
        
        query_insert="INSERT INTO dates (tittle,description,status) VALUES ('%s','%s','1');" % (title,description)
        with engine.connect() as connection:
            connection.execute(query_insert)
            return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    print(id)
    if not id or id != 0:
        
        query_delete="DELETE FROM dates WHERE id=%s " % (id)
        with engine.connect() as connection:
            connection.execute(query_delete)
            return redirect('/')

@app.route('/turn/<int:id>')
def turn(id):
    if not id or id != 0:
        query_turn="UPDATE dates SET status='0' WHERE id=%s" %(id)
        with engine.connect() as connection:
            connection.execute(query_turn)
            return redirect('/')

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    if request.method == 'POST':
        if not id or id != 0:
            form=request.form
            title=str(form.get('title'))
            description=str(form.get('description'))
            
            query_insert="UPDATES dates SET tittle='%s', description='%s'WHERE id=%s;" % (title,description,id)
            with engine.connect() as connection:
                connection.execute(query_insert)
                return redirect('/')
    if request.method=='GET':
        with engine.connect() as connection:
                entry=connection.execute("SELECT * FROM dates WHERE id=%s" %(id))
                return render_template('update.html', entry=entry)
       

if __name__ == '__main__':
    app.run(debug=True)

