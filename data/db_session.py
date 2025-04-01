from flask_login import UserMixin
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

DATABASE_URL = 'sqlite:///db/data.db'

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)


def create_session():
    return Session()


class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password_hash = Column(String)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


Base.metadata.create_all(engine)
