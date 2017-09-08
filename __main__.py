from optparse import OptionParser


class BruteForceLogin:
    url = ''
    dict_name = ''
    username = ''
    passname = ''

    def execute(self):
        self.get_args()

        self.print_welcome()

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
        url = options.url
        dict_name = options.dict
        username = options.username
        passname = options.passname

    def print_welcome(self):
        print("Bienvenue à BruteForceLogin!")


if __name__ == '__main__':
    brute_force_login = BruteForceLogin()
    brute_force_login.execute()
