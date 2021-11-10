import os
import csv
from copy import deepcopy

from marshmallow import Schema, fields, pre_load
from marshmallow.validate import Length, Range


class UserSchema(Schema):
    """Represent a *valid* user."""
    email = fields.Email(required=True)
    name = fields.String(required=True, validate=Length(min=1))
    age = fields.Integer(required=True, validate=Range(min=18, max=65))
    role = fields.String()

    @pre_load(pass_many=False)
    def strip_name(self, data):
        data_copy = deepcopy(data)

        try:
            data_copy['name'] = data_copy['name'].strip()
        except (AttributeError, KeyError, TypeError):
            pass

        return data_copy


schema = UserSchema()


def export(filename, users, overwrite=True):
    if not overwrite and os.path.isfile(filename):
        raise IOError(f"'{filename}' already exists.")

    valid_users = get_valid_users(users)
    write_csv(filename, valid_users)


def get_valid_users(users):
    yield from filter(is_valid, users)


def is_valid(user):
    return not schema.validate(user)


def write_csv(filename, users):
    fieldnames = ['email', 'name', 'age', 'role']

    with open(filename, 'x', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for user in users:
            writer.writerow(users)