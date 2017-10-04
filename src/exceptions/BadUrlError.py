from src.Messages import Messages


class BadUrlError(Exception):

    def __init__(self):
        print(Messages.URL_NOT_FOUND)
