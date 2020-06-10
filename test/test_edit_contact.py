from model.contact import Contact
import random


def test_edit_contact_by_index(app, db):
    contact = Contact(firstname="nameEdited", middlename="Edited", lastname="ZEdited",
                      nickname="Edited", title="Edited",
                      company="Edited", address="Edited", home="321", mobile="654",
                      work="987",
                      fax="Edited",
                      email="edited@komail.com", homepage="www.yandex.com", bday="10",
                      bmonth="December",
                      byear="2010",
                      aday="1", amonth="September", ayear="2007", address2="Edited",
                      phone2="890",
                      notes="Edited")
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(
            Contact(bday="3", bmonth="August", aday="13", amonth="July"))
    old_contacts = db.get_contact_list()
    modified_contact = random.choice(old_contacts)
    contact.id = modified_contact.id
    app.contact.edit_contact_by_id(contact, contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    new_contacts = db.get_contact_list()
    index = old_contacts.index(modified_contact)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
