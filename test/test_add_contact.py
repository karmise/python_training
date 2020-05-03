# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from fixture.contacting import Contacting


@pytest.fixture
def cont(request):
    fixture = Contacting()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(cont):
    cont.open_home_page()
    cont.login(username="admin", password="secret")
    cont.add_new_contact_page()
    cont.fill_contact_page(Contact(firstname="tqwet", middlename="twet", lastname="sdgsg", nickname="fsdfsdf",
                                   title="fasfa",
                                   company="fasfasf", address="asgasg", home="gsdgg", mobile="5256626", work="wrwer",
                                   fax="qwrqwr",
                                   email="ututut@komail.com", homepage="www.google.com", bday="13", bmonth="May",
                                   byear="1990",
                                   aday="18", amonth="June", ayear="2005", address2="gagag", phone2="near",
                                   notes="votes"))
    cont.submit_contact_creation()
    cont.return_to_home_page()
    cont.logout()


def test_add_empty_contact(cont):
    cont.open_home_page()
    cont.login(username="admin", password="secret")
    cont.add_new_contact_page()
    cont.fill_contact_page(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                   address="", home="", mobile="", work="", fax="", email="", homepage="", bday="10",
                                   bmonth="October", byear="2012", aday="30", amonth="December", ayear="1998",
                                   address2="",
                                   phone2="", notes=""))
    cont.submit_contact_creation()
    cont.return_to_home_page()
    cont.logout()
