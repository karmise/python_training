from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_new_contact(self, new_contact):
        self.add_new_contact_page()
        self.fill_contact_page(new_contact)
        self.submit_contact_creation()
        self.return_to_home_page()
        self.contact_cache = None

    def add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_page(self, contact):
        wd = self.app.wd
        self.change_field("firstname", contact.firstname)
        self.change_field("middlename", contact.middlename)
        self.change_field("lastname", contact.lastname)
        self.change_field("nickname", contact.nickname)
        self.change_field("title", contact.title)
        self.change_field("company", contact.company)
        self.change_field("address", contact.address)
        self.change_field("home", contact.home)
        self.change_field("mobile", contact.mobile)
        self.change_field("work", contact.work)
        self.change_field("fax", contact.fax)
        self.change_field("email", contact.email)
        self.change_field("email2", contact.email2)
        self.change_field("email3", contact.email3)
        self.change_field("homepage", contact.homepage)
        self.change_field("address2", contact.address2)
        self.change_field("phone2", contact.phone2)
        self.change_field("byear", contact.byear)
        self.change_field("ayear", contact.ayear)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("amonth").click()

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        self.return_to_home_page()
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        # submit deletion
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_contact_to_edit_by_index(self, index):
        self.return_to_home_page()
        wd = self.app.wd
        elements = wd.find_elements_by_xpath("//img[@alt='Edit']")
        elements[index].click()

    def select_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

    def edit_first_contact(self):
        self.select_contact_by_index(0)

    def edit_contact_by_index(self, index, cont):
        self.return_to_home_page()
        self.select_contact_to_edit_by_index(index)
        self.fill_contact_page(cont)
        self.submit_contact_edition()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, cont):
        self.return_to_home_page()
        self.select_contact_to_edit_by_id(id)
        self.fill_contact_page(cont)
        self.submit_contact_edition()
        self.return_to_home_page()
        self.contact_cache = None

    def submit_contact_edition(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/index.php"):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            for elements in wd.find_elements_by_name("entry"):
                cells = elements.find_elements_by_tag_name("td")
                first_name = elements.find_element_by_xpath("td[3]").text
                last_name = elements.find_element_by_xpath("td[2]").text
                address = elements.find_element_by_xpath("td[4]").text
                all_emails = cells[4].text
                id = elements.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(
                    Contact(firstname=first_name, lastname=last_name, id=id,
                            all_phones_from_home_page=all_phones, address=address,
                            all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home=home, mobile=mobile, work=work, phone2=phone2,
                       address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)

    def add_contact_to_group(self, contact, add_to_group):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_id(contact.id)
        wd.find_element_by_css_selector('select[name="to_group"]').click()
        wd.find_element_by_css_selector('select[name="to_group"] option[value="%s"]' % add_to_group.id).click()
        wd.find_element_by_css_selector('input[value="Add to"]').click()
        self.return_to_home_page()

    def del_contact_from_group(self, contact, add_to_group):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element_by_css_selector('select[name="group"]').click()
        wd.find_element_by_css_selector('select[name="group"] option[value="%s"]' % add_to_group.id).click()
        self.select_contact_by_id(contact.id)
        wd.find_element_by_css_selector('input[name="remove"]').click()
        self.return_to_home_page()



