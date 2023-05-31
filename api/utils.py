from api.models import User
import faker
from datetime import datetime
faker = faker.Faker('Fr-fr')


class GenerateFaker:
    def __init__(self, group=""):
        self.first_name = faker.first_name()
        self.last_name = faker.last_name()
        self.tel = faker.phone_number()
        self.mobile = faker.phone_number()
        self.is_active = True
        self.email = faker.email()
        self.password = "Thomas404*"
        self.role = group

    def get_group_data(self):
        if self.role == "MANAGEMENT":
            is_admin = True
        else:
            is_admin = False
        return {
            'email': self.email,
            'password': self.password,
            'password2': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role,
            'tel': self.tel,
            'is_active': self.is_active,
            'is_admin': is_admin,
        } if self.role in ["MANAGEMENT", "SALES", "SUPPORT"] else {}

    def get_simplified_group_data(self):
        if self.role == "MANAGEMENT":
            is_admin = True
        else:
            is_admin = False
        return {
            'id': 1,
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role,
            'tel': self.tel,
            'is_active': self.is_active,
            'is_admin': is_admin,
        } if self.role in ["MANAGEMENT", "SALES", "SUPPORT"] else {}

    def get_client(self):
        return {
            'id': 1,
            'is_prospect': True,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'tel': self.tel,
            'mobile': self.mobile,
            'company_name': faker.company(),
            'twitter': faker.user_name(),
            'facebook': faker.user_name(),
            'linkedin': faker.user_name()

        }

    def get_contract(self):
        return {
            'id': 2,
            'status': True,
            'amount': faker.pyfloat(min_value=0.0, max_value=1000.0, right_digits=2),
            'payement_due' : faker.date(),
            'date_updated': datetime.now()
        }

    def get_event(self):
        return {
            'attendees' : faker.pyint(min_value=1, max_value=100),
            'client_id' : faker.pyint(min_value=1, max_value=100),
            'support_contact_id': faker.pyint(min_value=1, max_value=100),
            'notes': faker.text(),
            'event_date': faker.date(),
        }

