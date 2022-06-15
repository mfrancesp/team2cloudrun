from flask import Flask
import pymysql 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine

app = Flask(__name__)


# Google Cloud SQL (change this accordingly)
PASSWORD ="secretpassword"
PUBLIC_IP_ADDRESS ="35.205.41.62"
DBNAME ="testing"
PROJECT_ID ="team2-353417"
INSTANCE_NAME ="databaseuser"
 
# configuration
app.config["SECRET_KEY"] = "secretpassword"
app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql+pymysql://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
 
db = SQLAlchemy(app)

class data(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    tittle = db.Column(db.String(64), nullable = False)
    description = db.Column(db.String(120), nullable = False, unique = True)
    status = db.Column(db.Boolean())
    
#db.create_all()

engine = create_engine(f"mysql+pymysql://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket =/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}")

#connection=create_engine.connect()
from app import routes, models
