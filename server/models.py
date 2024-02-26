from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Company(db.Model, SerializerMixin):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    founder = db.Column(db.String)
    founding_date = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f"<Company: {self.name}, Founder: {self.founder}>"
