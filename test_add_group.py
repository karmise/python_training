# -*- coding: utf-8 -*-
import unittest
from group import Group
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


def open_home_page(self):
    wd = self.wd
    wd.get("http://localhost/addressbook/index.php")


def login(self, username, password):
    wd = self.wd
    open_home_page(self)
    wd.find_element_by_name("user").click()
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys(username)
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys(password)
    wd.find_element_by_xpath("//input[@value='Login']").click()


def open_groups_page(self):
    wd = self.wd
    wd.find_element_by_link_text("groups").click()


def create_group(self, group):
    wd = self.wd
    open_groups_page(self)
    # init group creation
    wd.find_element_by_name("new").click()
    # fill group form
    wd.find_element_by_name("group_name").click()
    wd.find_element_by_name("group_name").clear()
    wd.find_element_by_name("group_name").send_keys(group.name)
    wd.find_element_by_name("group_header").click()
    wd.find_element_by_name("group_header").clear()
    wd.find_element_by_name("group_header").send_keys(group.header)
    wd.find_element_by_name("group_footer").click()
    wd.find_element_by_name("group_footer").clear()
    wd.find_element_by_name("group_footer").send_keys(group.footer)
    # submit group creation
    wd.find_element_by_name("submit").click()
    return_to_groups_page(self)


def return_to_groups_page(self):
    wd = self.wd
    wd.find_element_by_link_text("group page").click()


def logout(self):
    wd = self.wd
    wd.find_element_by_link_text("Logout").click()


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        login(self, username="admin", password="secret")
        create_group(self, Group(name="fwegwg", header="sdsdgsdg", footer="sdgwet"))
        logout(self)

    def test_add_empty_group(self):
        login(self, username="admin", password="secret")
        create_group(wd, Group(name="", header="", footer=""))
        logout(self)

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
