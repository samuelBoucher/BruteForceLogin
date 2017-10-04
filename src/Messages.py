class Messages:
    ENTER_USERNAME = "Entrez le nom de l'utilisateur pour qui vous voulez trouver le mot de passe: "
    USERNAME_NOT_FOUND = "Aucun mot de passe n'a été trouvé pour l'utilisateur "
    CLOSING_APPLICATION = ", fermeture de l'application"
    FIELD_NAME_NOT_FOUND = "Le formulaire avec les noms de champs spécifiés sont introuvables, fermeture de l'application"
    PASSWORD_FOUND = "Mot de passe trouvé en "
    MINUTES = " minutes: "
    PASSWORD = "Le mot de passe "
    HASNT_WORKED = " n\'a pas fonctionné..."

    @staticmethod
    def print_url_not_found(url):
        return "L'url " + url + " n\'a pas été trouvé"

    @staticmethod
    def print_dict_not_found(path):
        return "Le dictionaire situé au chemin " + path + " n\'a pas été trouvé"

    @staticmethod
    def print_form_not_found(username, passname):
        return "Le formulaire avec le nom de champ d\'utilisateur \'" + username + "\'\n " \
                "et le nom de champ de mot de passe \'" + passname + "\'\n " \
                "n\'a pas été trouvé"

