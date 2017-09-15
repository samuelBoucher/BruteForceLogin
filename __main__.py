from optparse import OptionParser
from DictionaryReader import DictionaryReader
from time import time

class BruteForceLogin:
    url = ''
    dict_name = ''
    username = ''
    passname = ''

    start = 0
    end = 0


    def execute(self):
        self.get_args()
        self.print_welcome()
        dictionary_reader = DictionaryReader(self.dict_name)
        passwords = dictionary_reader.read()
        for password in passwords:
            print(password)

    def get_args(self):
        parser = self.get_parser()
        (options, args) = parser.parse_args()
        self.set_attributes(options)

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

    def print_welcome(self):
        print("Bienvenue à BruteForceLogin!")


if __name__ == '__main__':
    brute_force_login = BruteForceLogin()
    brute_force_login.execute()
