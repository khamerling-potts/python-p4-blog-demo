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

    def post(self):
        data = request.get_json()
        try:
            # Attempting to create a Company instance with the data from the request body
            new_company = Company(name=data.get("name"), founder=data.get("founder"))

            # Attempting to add and commit the new instance to the db
            db.session.add(new_company)
            db.session.commit()

            # Returning a response with our new company (serialized) and a status code
            return new_company.to_dict(), 201
        except:
            return {"error": "422 - Unprocessable Entity"}, 422


api.add_resource(Companies, "/companies", endpoint="companies")


class CompanyByID(Resource):
    def get(self, id):
        company = Company.query.filter_by(id=id).first()
        if company:
            return company.to_dict(), 200
        return {"error": "404 - Company not found"}, 404


api.add_resource(CompanyByID, "/companies/<int:id>", endpoint="company")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
