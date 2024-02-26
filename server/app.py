#!/usr/bin/env python3

from flask import Flask, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Company

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///companies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

# Constructor for your API, initialized with a Flask application instance.
# Will populate with Resources (as we define below)
api = Api(app)

# ADDING RESOURCES BELOW:


class Companies(Resource):
    def get(self):
        # Query database here, serializing each Company with to_dict()
        companies = [company.to_dict() for company in Company.query.all()]
        return companies, 200


api.add_resource(Companies, "/companies", endpoint="companies")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
