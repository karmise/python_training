import re
from model.contact import Contact


def test_match_contact_on_home_page(app, db):
    all_ui_contacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    all_db_contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    i = 0
    for contact in all_ui_contacts:
        contact_from_db = all_db_contacts_from_db[i]
        i = i + 1
        assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)
        assert contact.firstname == contact_from_db.firstname
        assert contact.lastname == contact_from_db.lastname
        assert contact.address == contact_from_db.address


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter
    (lambda x: x is not None, [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter
    (lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))
