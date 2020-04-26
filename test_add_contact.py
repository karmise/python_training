# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


def open_home_page(wd):
    wd.get("http://localhost/addressbook/index.php")


def login(wd, username, password):
    wd.find_element_by_name("user").click()
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys(username)
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys(password)
    wd.find_element_by_xpath("//input[@value='Login']").click()


def add_new_contact_page(wd):
    wd.find_element_by_link_text("add new").click()


def fill_contact_page(wd, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work, fax,
                      email, homepage, bday, bmonth, byear, aday, amonth, ayear, address2, phone2, notes):
    wd.find_element_by_name("firstname").click()
    wd.find_element_by_name("firstname").clear()
    wd.find_element_by_name("firstname").send_keys(firstname)
    wd.find_element_by_name("middlename").clear()
    wd.find_element_by_name("middlename").send_keys(middlename)
    wd.find_element_by_name("lastname").clear()
    wd.find_element_by_name("lastname").send_keys(lastname)
    wd.find_element_by_name("nickname").clear()
    wd.find_element_by_name("nickname").send_keys(nickname)
    wd.find_element_by_name("title").click()
    wd.find_element_by_name("title").clear()
    wd.find_element_by_name("title").send_keys(title)
    wd.find_element_by_name("company").click()
    wd.find_element_by_name("company").clear()
    wd.find_element_by_name("company").send_keys(company)
    wd.find_element_by_name("address").click()
    wd.find_element_by_name("address").clear()
    wd.find_element_by_name("address").send_keys(address)
    wd.find_element_by_name("home").clear()
    wd.find_element_by_name("home").send_keys(home)
    wd.find_element_by_name("mobile").clear()
    wd.find_element_by_name("mobile").send_keys(mobile)
    wd.find_element_by_name("work").clear()
    wd.find_element_by_name("work").send_keys(work)
    wd.find_element_by_name("fax").clear()
    wd.find_element_by_name("fax").send_keys(fax)
    wd.find_element_by_name("email").clear()
    wd.find_element_by_name("email").send_keys(email)
    wd.find_element_by_name("homepage").click()
    wd.find_element_by_name("homepage").clear()
    wd.find_element_by_name("homepage").send_keys(homepage)
    Select(wd.find_element_by_name("bday")).select_by_visible_text(bday)
    wd.find_element_by_name("bday").click()
    Select(wd.find_element_by_name("bmonth")).select_by_visible_text(bmonth)
    wd.find_element_by_name("bmonth").click()
    wd.find_element_by_name("byear").click()
    wd.find_element_by_name("byear").clear()
    wd.find_element_by_name("byear").send_keys(byear)
    Select(wd.find_element_by_name("aday")).select_by_visible_text(aday)
    wd.find_element_by_name("aday").click()
    Select(wd.find_element_by_name("amonth")).select_by_visible_text(amonth)
    wd.find_element_by_name("amonth").click()
    wd.find_element_by_name("ayear").click()
    wd.find_element_by_name("ayear").clear()
    wd.find_element_by_name("ayear").send_keys(ayear)
    wd.find_element_by_name("address2").click()
    wd.find_element_by_name("address2").clear()
    wd.find_element_by_name("address2").send_keys(address2)
    wd.find_element_by_name("phone2").click()
    wd.find_element_by_name("phone2").clear()
    wd.find_element_by_name("phone2").send_keys(phone2)
    wd.find_element_by_name("notes").click()
    wd.find_element_by_name("notes").clear()
    wd.find_element_by_name("notes").send_keys(notes)


def submit_contact_creation(wd):
    wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


def return_to_home_page(wd):
    wd.find_element_by_link_text("home page").click()


def logout(wd):
    wd.find_element_by_link_text("Logout").click()


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        open_home_page(wd)
        login(wd, username="admin", password="secret")
        add_new_contact_page(wd)
        fill_contact_page(wd, firstname="tqwet", middlename="twet", lastname="sdgsg", nickname="fsdfsdf", title="fasfa",
                          company="fasfasf", address="asgasg", home="gsdgg", mobile="5256626", work="wrwer",
                          fax="qwrqwr",
                          email="ututut@komail.com", homepage="www.google.com", bday="13", bmonth="May", byear="1990",
                          aday="18", amonth="June", ayear="2005", address2="gagag", phone2="near", notes="votes")
        submit_contact_creation(wd)
        return_to_home_page(wd)
        logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        open_home_page(wd)
        login(wd, username="admin", password="secret")
        add_new_contact_page(wd)
        fill_contact_page(wd, firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                          home="", mobile="", work="", fax="", email="", homepage="", bday="10", bmonth="October",
                          byear="2012", aday="30", amonth="December", ayear="1998", address2="", phone2="", notes="")
        submit_contact_creation(wd)
        return_to_home_page(wd)
        logout(wd)

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
