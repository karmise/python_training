# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                    address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="",
                    bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="",
                    phone2="", notes="")] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                       lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                       title=random_string("title", 20), company=random_string("company", 10),
                       address=random_string("address", 20), home="+7111",
                       mobile="+72222", work="+7333",
                       fax="+74444", email=random_string("email", 20), email2=random_string("email2", 10),
                       email3=random_string("email3", 10),
                       homepage=random_string("homepage", 10), bday="11",
                       bmonth="May", byear="2010",
                       aday="13", amonth="September",
                       ayear="2020", address2=random_string("address2", 10),
                       phone2="+755555", notes=random_string("notes", 10), )
               for i in range(5)
           ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
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
