#!/usr/bin/env python3

from faker import Faker

from app import app
from models import db, Company


with app.app_context():

    fake = Faker()

    Company.query.delete()

    companies = []
    for i in range(10):
        company = Company(
            name=fake.text(max_nb_chars=20),
            founder=fake.name(),
            founding_date=fake.date_object(),
        )
        print(type(company.founding_date))
        companies.append(company)

    db.session.add_all(companies)
    db.session.commit()
