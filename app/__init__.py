from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
SERVICE_ACCOUNT="p265126880907-keyiyh@gcp-sa-cloud-sql.iam.gserviceaccount.com"
PASSWORD ="dreamteam"
PUBLIC_IP_ADDRESS ="34.77.51.214"
DBNAME ="simple-app-db"
PROJECT_ID ="cloudrunproject-group2"
INSTANCE_NAME ="cloudrunproject-group2:europe-west1:simple-app-db"
#SQLALCHEMY_DATABASE_URI = f'psql+psqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}'

SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{SERVICE_ACCOUNT}:{PASSWORD}@/{DBNAME}?host=/cloudsql/{PROJECT_ID}:europe-west1:{DBNAME}=tcp:5432"
#PASSWORD ="dreamteam"
#PUBLIC_IP_ADDRESS ="34.77.51.214"
#DBNAME ="simple-app-db"
#PROJECT_ID ="cloudrunproject-group2"
#INSTANCE_NAME ="cloudrunproject-group2:europe-west1:simple-app-db"
#SQLALCHEMY_DATABASE_URI = f'psql+psqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}'


# configuration
#app.config["SECRET_KEY"] = "LCi3laZzkuFwmATf2+APAKzW5sEZxSRjibYEW89x"
#app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True



engine = create_engine(SQLALCHEMY_DATABASE_URI)


from app import routes, models
