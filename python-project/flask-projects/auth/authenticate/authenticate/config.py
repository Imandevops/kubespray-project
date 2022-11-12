from os import environ

class Config:


    ENV = environ.get("ENV", "production")

    DEBUG = bool(int(environ.get("DEBUG", "0")))

    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URI", None)

    SQLALCHEMY_ECHO = DEBUG

    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG