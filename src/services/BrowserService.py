import requests
from robobrowser import RoboBrowser

from src.exceptions.BadUrlError import BadUrlError
from src.Messages import Messages


class BrowserService:

    def __init__(self, url):
        self.browser = RoboBrowser(parser='html.parser')
        self.base_url = url

        self.validate_url(url)

        self.browser.open(self.base_url)

    def validate_url(self, url):
        request = requests.get(url)
        if request.status_code != 200:
            message = Messages.get_url_not_found_message(url)
            raise BadUrlError(message)

    def get_form(self, form_name):
        return self.browser.get_form(form_name)

    def verify_url_has_changed(self):
        return self.base_url != self.browser.url

    def submit_form(self, form):
        self.browser.submit_form(form)
