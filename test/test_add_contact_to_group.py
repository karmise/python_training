from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create_new_contact(
            Contact(bday="3", bmonth="August", aday="13", amonth="July"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    all_groups = orm.get_group_list()
    group = random.choice(all_groups)
    all_contacts = orm.get_contact_list()
    contact = random.choice(all_contacts)
    if contact in (orm.get_contacts_in_group(group)):
        app.contact.delete_contact_from_group(contact, group)
    app.contact.add_contact_to_group(contact, group)
    assert contact in orm.get_contacts_in_group(group)
