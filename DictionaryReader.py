from os.path import exists


class DictionaryReader:
    dictionaries_root = "Dictionaries\\"
    dict_name = ''

    def __init__(self, dict_name):
        self.dict_name = dict_name

    def read(self):
        path = self.dictionaries_root + self.dict_name
        if exists(path):
            print("ok")
        else:
            print("Dictionaire introuvable...")




