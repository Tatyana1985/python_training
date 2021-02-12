# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException
import unittest
from name_data import Name_data
from job_data import Job_data
from telephone_data import Telephone_data
from email_data import Email_data
from date_data import Date_data

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except NoAlertPresentException as e:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_new_page(wd)
        self.enter_name_data(wd, Name_data(firstname="asdfg", middlename="asdfg", lastname="asdfg", nickname="asdfg"))
        self.enter_job_data(wd, Job_data(title="asdfg", company="asdfg", address="asdfg"))
        self.enter_telephone_data(wd, Telephone_data(home="565656", mobile="677565", work="76876687", fax="67678678"))
        self.enter_email_data(wd, Email_data(email="rert@uyuy.try", email2="rtrt@tyty.tyty", email3="rtr@uiui.tyt", homepage="trtr@yuu.uyu"))
        self.enter_birthday(wd, Date_data(day="7", month="August", year="2000"))
        self.click_enter(wd)
        self.click_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def click_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def click_enter(self, wd):
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def enter_birthday(self, wd, date_data):
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("7")
        wd.find_element_by_xpath("//option[@value='" + date_data.day + "']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(date_data.month)
        wd.find_element_by_xpath("//option[@value='" + date_data.month + "']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(date_data.year)

    def enter_email_data(self, wd, email_data):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email_data.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email_data.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email_data.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(email_data.homepage)

    def enter_telephone_data(self, wd, telephone_data):
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(telephone_data.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(telephone_data.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(telephone_data.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(telephone_data.fax)

    def enter_job_data(self, wd, job_data):
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(job_data.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(job_data.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(job_data.address)

    def enter_name_data(self, wd, name_data):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(name_data.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(name_data.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(name_data.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(name_data.nickname)

    def open_add_new_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
