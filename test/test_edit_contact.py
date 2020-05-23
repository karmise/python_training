from model.contact import Contact
from random import randrange


def test_edit_contact_by_index(app):
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
    if app.contact.count() == 0:
        app.contact.create_new_contact(
            Contact(bday="3", bmonth="August", aday="13", amonth="July"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
