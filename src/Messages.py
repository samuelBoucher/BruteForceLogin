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
    def get_url_not_found_message(url):
        return "L'url " + url + " n\'a pas été trouvé"

    @staticmethod
    def get_dict_not_found_message(path):
        return "Le dictionaire situé au chemin " + path + " n\'a pas été trouvé"

    @staticmethod
    def get_form_not_found_message(user_field, password_field):
        return "Le formulaire avec le nom de champ d\'utilisateur \'" + user_field + "\'\n " \
                "et le nom de champ de mot de passe \'" + password_field + "\'\n " \
                "n\'a pas été trouvé"

    @staticmethod
    def print_username_not_found(username):
        print("Le mot de passe de l'utilisateur " + username + " n\' a pas été trouvé")

    @staticmethod
    def print_password_found(minutes_elapsed, password):
        print("Mot de passe trouvé en " + minutes_elapsed + " minutes: " + password)

    @staticmethod
    def print_password_unsuccessful(password):
        print("Le mot de passe " + password + " n'a pas fonctionné...")

