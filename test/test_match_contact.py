import re
from model.contact import Contact


def test_match_contact_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contact_from_home_page)):
        assert contact_from_home_page[i] == contact_from_db[i]


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter
                            (lambda x: x is not None, [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter
                            (lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))