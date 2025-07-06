import os
from dotenv import load_dotenv

load_dotenv()

db_schema = os.getenv("db_schema")
db_username = os.getenv("db_username")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")


main_db_uri = (
    "postgresql+psycopg2://"
    + db_username
    + ":"
    + db_password
    + "@"
    + db_host
    + ":5432/"
    + db_schema
)


class Config:
    SQLALCHEMY_DATABASE_URI = main_db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False

