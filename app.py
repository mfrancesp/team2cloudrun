from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask import render_template, request, redirect
from flask_migrate import Migrate
from sqlalchemy import create_engine
#import mysql.connector

app = Flask(__name__)
PASSWORD ="secretpassword"
PUBLIC_IP_ADDRESS ="35.205.41.62"
DBNAME ="testing"
PROJECT_ID ="team2-353417"
INSTANCE_NAME ="team2-353417:europe-west1:databaseuser"
SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}'
# configuration
app.config["SECRET_KEY"] = "zwBhXws0knq7dZ6f0ciIK3fl5cefusJRtFEiU5Hi"
app.config["SQLALCHEMY_DATABASE_URI"]= SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True


db = SQLAlchemy(app)
class dates(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tittle = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.String(120), index=True, nullable=False)
    status = db.Column(db.Boolean, default=False)
    extend_existing=True

    
db.create_all()

engine = create_engine(SQLALCHEMY_DATABASE_URI)
#connection = mysql.connector.connect(user='root',password='secretpassword', host='35.205.41.62',datase='testing')
#connection=create_engine.connect()
#cursor=connection.cursor()
connection=engine.connect()


@app.route('/')
@app.route('/index')
def index():
    # entries = [
    #     {
    #         'id' : 1,
    #         'title': 'test title 1',
    #         'description' : 'test desc 1',
    #         'status' : True
    #     },
    #     {
    #         'id': 2,
    #         'title': 'test title 2',
    #         'description': 'test desc 2',
    #         'status': False
    #     }
    # ]
    insert_brochure_query = """
    SELECT * FROM dates
    """
    with engine.connect() as connection:
        entries=connection.execute(insert_brochure_query)
        return render_template('index.html', entries=entries)

    #entries = connection.query.all()
    #return render_template('index.html', entries=entries)
   

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        description = form.get('description')
        if not title or description:
            entry = dates(title = title, description = description)
            db.session.add(entry)
            db.session.commit()
            return redirect('/')

    return "of the jedi"

@app.route('/update/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        entry = dates.query.get(id)
        if entry:
            return render_template('update.html', entry=entry)

    return "of the jedi"

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if not id or id != 0:
        entry = dates.query.get(id)
        if entry:
            form = request.form
            title = form.get('title')
            description = form.get('description')
            entry.title = title
            entry.description = description
            db.session.commit()
        return redirect('/')

    return "of the jedi"



@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entry = dates.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return "of the jedi"

@app.route('/turn/<int:id>')
def turn(id):
    if not id or id != 0:
        entry = dates.query.get(id)
        if entry:
            entry.status = not entry.status
            db.session.commit()
        return redirect('/')

    return "of the jedi"

@app.errorhandler(Exception)
def error_page(e):
    return "error"

if __name__ == '__main__':
    app.run()
#import app.routes
