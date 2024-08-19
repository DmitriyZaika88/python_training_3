

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_creation_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_contact_creation_page()
        # form block edition begins
        self.fill_contact_form(contact)
        # form block edition end
        self.sumbit_contact_creation()
        self.return_to_home_page()

    def change_contact_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_field_value("firstname", contact.first_name)
        self.change_contact_field_value("middlename", contact.middle_name)
        self.change_contact_field_value("lastname", contact.last_name)
        self.change_contact_field_value("nickname", contact.nickname)
        self.change_contact_field_value("title", contact.title)
        self.change_contact_field_value("company", contact.company)
        self.change_contact_field_value("address", contact.address)
        self.change_contact_field_value("home", contact.home)
        self.change_contact_field_value("mobile", contact.mobile)
        self.change_contact_field_value("work", contact.work)
        self.change_contact_field_value("fax", contact.fax)
        self.change_contact_field_value("email", contact.email_1)
        self.change_contact_field_value("email2", contact.email_2)
        self.change_contact_field_value("email3", contact.email_3)
        self.change_contact_field_value("homepage", contact.homepage)
        # date of birth field
        self.change_contact_field_value("bday", contact.day_of_birth)
        self.change_contact_field_value("bmonth", contact.month_of_birth)
        self.change_contact_field_value("byear", contact.year_of_birth)
        # anniversary field
        self.change_contact_field_value("aday", contact.anniversary_day)
        self.change_contact_field_value("amonth", contact.anniversary_month)
        self.change_contact_field_value("ayear", contact.anniversary_year)
        # wd.find_element_by_name("theform").click()

    def sumbit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        # select first checkbox contact
        wd.find_element_by_name("selected[]").click()
        # delete first checkbox contact
        wd.find_element_by_css_selector("input[value='Delete']").click()

    def open_contact_edition_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        self.open_contact_edition_page()
        # clear personal_information_fields
        self.fill_contact_form(new_contact_data)
        self.update_contact_confirmation()
        self.return_to_home_page()

    def update_contact_confirmation(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def count_contact_first_name(self):
        wd = self.app.wd
        self.open_contact_page()
        self.open_contact_edition_page()
        return len(wd.find_elements_by_name("first_name")) != ""
