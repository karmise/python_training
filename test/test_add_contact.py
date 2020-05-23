# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="tqwet", middlename="twet", lastname="sdgsg", nickname="fsdfsdf",
                      title="fasfa",
                      company="fasfasf", address="asgasg", home="123", mobile="456",
                      work="789",
                      fax="qwrqwr",
                      email="ututut@komail.com", homepage="www.google.com", bday="13",
                      bmonth="May",
                      byear="1990",
                      aday="18", amonth="June", ayear="2005", address2="gagag", phone2="098",
                      notes="votes")
    app.contact.create_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
#                      address="", home="", mobile="", work="", fax="", email="", homepage="",
#                      bday="10",
#                      bmonth="October", byear="2012", aday="30", amonth="December", ayear="1998",
#                      address2="",
#                      phone2="", notes="")
#    app.contact.create_new_contact(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
