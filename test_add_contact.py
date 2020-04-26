# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        # open_home_page
        wd.get("http://localhost/addressbook/index.php")
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        # open_add_contact_page
        wd.find_element_by_link_text("add new").click()
        # fill_contact_page
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("tqwet")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("twet")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("sdgsg")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("fsdfsdf")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("fasfa")
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("fasfasf")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("asgasg")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("gsdgg")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("5256626")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("wrwer")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("qwrqwr")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("ututut@komail.com")
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("www.google.com")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("13")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("May")
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")
        Select(wd.find_element_by_name("aday")).select_by_visible_text("18")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("June")
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2005")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("gagag")
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("near")
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("votes")
        # submit_contact_creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # return_to_home_page
        wd.find_element_by_link_text("home page").click()
        # logout
        wd.find_element_by_link_text("Logout").click()

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
