from optparse import OptionParser
from DictionaryReader import DictionaryReader
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
from httplib2 import Http
import sys
from time import time

class BruteForceLogin:
    url = ''
    dict_name = ''
    username = ''
    passname = ''

    def __init__(self):
        self.print_welcome()
        self.get_args()
        passwords = self.read_dictionary()
        self.brute_force_login()

    def print_welcome(self):
        print("Bienvenue à BruteForceLogin!")

    def get_args(self):
        parser = self.get_parser()
        (options, args) = parser.parse_args()
        self.set_attributes(options)

    # En faire une classe
    def get_parser(self):
        parser = OptionParser()
        parser.add_option("-r", "--url", dest="url")
        parser.add_option("-d", "--dict", dest="dict")
        parser.add_option("-u", "--username", dest="username")
        parser.add_option("-p", "--passname", dest="passname")
        return parser

    def set_attributes(self, options):
        self.url = options.url
        self.dict_name = options.dict
        self.username = options.username
        self.passname = options.passname

    def read_dictionary(self):
        dictionary_reader = DictionaryReader(self.dict_name)
        passwords = dictionary_reader.read()
        return passwords

    # En faire une classe
    def brute_force_login(self):
        browser = RoboBrowser(history=True)
        browser.open(self.url)
        all_forms = browser.get_forms()
        form_name = self.get_form_name()

    def get_form_name(self):
        http = Http('.cache')
        response, content = http.request('http://altoromutual.com/bank/login.aspx')
        forms = BeautifulSoup(content, "html.parser").findAll('form')

        for form in forms:
            str_form = form.prettify()
            if self.username in str_form and self.passname in str_form:
                str_after_name = str_form.split("name=\"", 1)[1]  # ex: <form name="uid" id="id">
                                                                 # devient
                                                                 #  uid" id="id">

                return str_after_name.split("\"", 1)[0]  # ex: uid" id="id">
                                                         # devient
                                                         # uid

        print("Le formulaire avec les noms de champs spécifiés sont introuvables, fermeture de l'application")
        sys.exit(1)


if __name__ == '__main__':
    brute_force_login = BruteForceLogin()
