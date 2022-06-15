import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
        

    PASSWORD ="dreamteam"
    PUBLIC_IP_ADDRESS ="34.77.51.214"
    DBNAME ="simple-app-db"
    PROJECT_ID ="cloudrunproject-group2"
    INSTANCE_NAME ="cloudrunproject-group2:europe-west1:simple-app-db"
    SERVICE_ACCOUNT="p265126880907-keyiyh@gcp-sa-cloud-sql.iam.gserviceaccount.com"
    db_socket_dir = "34.77.51.214/cloudsql"
    #SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{SERVICE_ACCOUNT}:{PASSWORD}@/{DBNAME}?host=/cloudsql/{PROJECT_ID}:europe-west1:{DBNAME}=tcp:5432"

    SQLALCHEMY_DATABASE_URI = f"postgresql+pg8000://{SERVICE_ACCOUNT}:{PASSWORD}@/{DBNAME}?unix_sock={db_socket_dir}/{INSTANCE_NAME}/.s.PGSQL.5432"
    # configuration
    SECRET_KEY = "LCi3laZzkuFwmATf2+APAKzW5sEZxSRjibYEW89x"
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{SERVICE_ACCOUNT}:{PASSWORD}@/{DBNAME}?host=/cloudsql/{PROJECT_ID}:europe-west1:{DBNAME}=tcp:5432"

    #SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS= True

    #SECRET_KEY = 'do-or-do-not-there-is-no-try'
    #    SECRET_KEY = os.environ.get('SECRET_KEY') or 'do-or-do-not-there-is-no-try'
     #   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
   #     SQLALCHEMY_TRACK_MODIFICATIONS = False