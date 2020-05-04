from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact()
    app.contact.fill_contact_page(
        Contact(firstname="nameEdited", middlename="Edited", lastname="Edited", nickname="Edited",
                title="Edited",
                company="Edited", address="Edited", home="Edited", mobile="777777",
                work="Edited",
                fax="Edited",
                email="edited@komail.com", homepage="www.yandex.com", bday="10", bmonth="December",
                byear="2010",
                aday="1", amonth="September", ayear="2007", address2="Edited", phone2="Edited",
                notes="Edited"))
    app.contact.submit_contact_edition()
    app.contact.return_to_home_page()
    app.session.logout()
