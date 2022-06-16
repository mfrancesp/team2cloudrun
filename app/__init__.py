from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
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


#db = SQLAlchemy(app)


    
#db.create_all()

engine = create_engine(SQLALCHEMY_DATABASE_URI)
#connection = mysql.connector.connect(user='root',password='secretpassword', host='35.205.41.62',datase='testing')
#connection=create_engine.connect()
#cursor=connection.cursor()
connection=engine.connect()
from app import routes, models
